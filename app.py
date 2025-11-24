import streamlit as st
import numpy as np
import sys
from pathlib import Path
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import tempfile
import os

sys.path.append(str(Path(__file__).parent))

from src.preprocessing.audio_processor import AudioProcessor
from src.features.feature_extractor import FeatureExtractor
from src.models.classifier import InstrumentClassifier
from src.models.dataset_manager import DatasetManager

st.set_page_config(
    page_title="Isan Musical Instruments Classifier",
    page_icon="🎵",
    layout="wide"
)

st.title("🎵 Traditional Isan Musical Instruments Classifier")
st.markdown("""
### Phin (พิณ) & Khaen (แคน) Recognition System

This application uses machine learning to identify and analyze traditional Isan musical instruments:
- **Phin (พิณ)**: A three-stringed lute from Northeastern Thailand
- **Khaen (แคน)**: A bamboo mouth organ, the national instrument of Laos

**Built with cultural respect and ethical AI practices**
""")

@st.cache_resource
def load_models():
    processor = AudioProcessor(target_sr=22050)
    extractor = FeatureExtractor(sr=22050)
    classifier = InstrumentClassifier()
    
    model_path = Path("models/instrument_classifier.pkl")
    if model_path.exists():
        classifier.load_model(str(model_path))
        return processor, extractor, classifier, True
    else:
        return processor, extractor, classifier, False

processor, extractor, classifier, model_loaded = load_models()

tab1, tab2, tab3, tab4 = st.tabs([
    "🎵 Classify Audio", 
    "📊 Dataset Management", 
    "📚 Documentation",
    "ℹ️ About"
])

with tab1:
    st.header("Audio Classification")
    
    if not model_loaded:
        st.warning("⚠️ No trained model found. Please train a model first using the training pipeline or add sample data.")
        st.info("""
        To get started:
        1. Use the Dataset Management tab to add audio samples
        2. Run the training pipeline to create a model
        3. Return here to classify new audio files
        """)
    else:
        st.success("✅ Model loaded successfully!")
        
        uploaded_file = st.file_uploader(
            "Upload an audio file (WAV, MP3, FLAC, OGG)", 
            type=['wav', 'mp3', 'flac', 'ogg']
        )
        
        if uploaded_file is not None:
            with tempfile.NamedTemporaryFile(delete=False, suffix='.wav') as tmp_file:
                tmp_file.write(uploaded_file.read())
                tmp_path = tmp_file.name
            
            try:
                col1, col2 = st.columns([1, 1])
                
                with col1:
                    st.subheader("Audio Analysis")
                    
                    with st.spinner("Processing audio..."):
                        audio, sr, quality = processor.preprocess_audio(tmp_path)
                    
                    st.write("**Audio Quality Metrics:**")
                    st.json({
                        'Duration': f"{quality['duration']:.2f} seconds",
                        'Sample Rate': f"{sr} Hz",
                        'RMS Energy': f"{quality['rms_energy']:.4f}",
                        'Max Amplitude': f"{quality['max_amplitude']:.4f}",
                        'Valid': quality['is_valid']
                    })
                    
                    if quality['is_valid']:
                        st.audio(uploaded_file, format='audio/wav')
                
                with col2:
                    if quality['is_valid']:
                        st.subheader("Classification Results")
                        
                        with st.spinner("Extracting features and predicting..."):
                            features = extractor.extract_all_features(audio)
                            prediction = classifier.predict_single(features)
                        
                        st.markdown(f"### Predicted Instrument: **{prediction['predicted_instrument']}**")
                        st.metric("Confidence", f"{prediction['confidence']*100:.2f}%")
                        
                        st.write("**All Probabilities:**")
                        prob_df = pd.DataFrame([
                            {'Instrument': k, 'Probability': f"{v*100:.2f}%"} 
                            for k, v in prediction['all_probabilities'].items()
                        ])
                        st.dataframe(prob_df, hide_index=True)
                        
                        fig = px.bar(
                            x=list(prediction['all_probabilities'].keys()),
                            y=[v*100 for v in prediction['all_probabilities'].values()],
                            labels={'x': 'Instrument', 'y': 'Probability (%)'},
                            title='Classification Probabilities'
                        )
                        st.plotly_chart(fig, use_container_width=True)
                    else:
                        st.error(f"Audio quality issue: {quality.get('reason', 'Unknown')}")
                
                if quality['is_valid']:
                    st.subheader("Feature Visualization")
                    
                    mfcc = extractor.extract_mfcc_features(audio)
                    spectral = extractor.extract_spectral_features(audio)
                    
                    col3, col4 = st.columns(2)
                    
                    with col3:
                        fig_mfcc = go.Figure()
                        fig_mfcc.add_trace(go.Bar(
                            y=mfcc['mfcc_mean'],
                            name='MFCC Mean'
                        ))
                        fig_mfcc.update_layout(
                            title='MFCC Coefficients',
                            xaxis_title='Coefficient Index',
                            yaxis_title='Value'
                        )
                        st.plotly_chart(fig_mfcc, use_container_width=True)
                    
                    with col4:
                        spectral_df = pd.DataFrame([
                            {'Feature': k, 'Value': v} 
                            for k, v in spectral.items()
                        ])
                        fig_spectral = px.bar(
                            spectral_df, x='Feature', y='Value',
                            title='Spectral Features'
                        )
                        fig_spectral.update_xaxes(tickangle=45)
                        st.plotly_chart(fig_spectral, use_container_width=True)
            
            finally:
                if os.path.exists(tmp_path):
                    os.unlink(tmp_path)

with tab2:
    st.header("Dataset Management")
    
    dataset_manager = DatasetManager()
    
    st.subheader("Add New Recording")
    
    with st.form("add_recording"):
        col1, col2 = st.columns(2)
        
        with col1:
            file_path = st.text_input("Audio File Path")
            instrument = st.selectbox("Instrument Type", ["Phin", "Khaen"])
            technique = st.text_input("Playing Technique")
        
        with col2:
            performer_name = st.text_input("Performer Name")
            consent = st.checkbox("Consent Obtained", value=False)
            cultural_attr = st.text_input("Cultural Attribution")
        
        notes = st.text_area("Additional Notes")
        
        submitted = st.form_submit_button("Add Recording")
        
        if submitted:
            if file_path and performer_name and cultural_attr:
                rec_id = dataset_manager.add_recording(
                    file_path=file_path,
                    instrument=instrument,
                    technique=technique,
                    performer_name=performer_name,
                    consent_status=consent,
                    cultural_attribution=cultural_attr,
                    notes=notes
                )
                st.success(f"Recording added successfully! ID: {rec_id}")
            else:
                st.error("Please fill in all required fields")
    
    st.subheader("Dataset Overview")
    
    df = dataset_manager.export_to_dataframe()
    if not df.empty:
        st.dataframe(df, use_container_width=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Instruments:**")
            instruments = dataset_manager.get_all_instruments()
            for inst in instruments:
                count = len(dataset_manager.get_recordings_by_instrument(inst))
                st.write(f"- {inst}: {count} recordings")
        
        with col2:
            st.write("**Consent Status:**")
            consent_stats = dataset_manager.validate_consent()
            st.json(consent_stats)
        
        st.write("**Cultural Attributions:**")
        cultural_summary = dataset_manager.get_cultural_summary()
        st.json(cultural_summary)
    else:
        st.info("No recordings in the dataset yet. Add some recordings above!")

with tab3:
    st.header("Documentation & Methodology")
    
    st.subheader("🎯 Project Overview")
    st.markdown("""
    This system is designed to recognize and analyze traditional Isan musical instruments using 
    machine learning techniques while maintaining cultural sensitivity and ethical practices.
    """)
    
    st.subheader("🎼 Instruments")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **Phin (พิณ)**
        - Three-stringed lute from Northeastern Thailand
        - Made from wood with a long neck
        - Produces melodic, resonant tones
        - Traditionally used in Mor Lam performances
        """)
    
    with col2:
        st.markdown("""
        **Khaen (แคน)**
        - Bamboo mouth organ
        - National instrument of Laos
        - Features multiple bamboo pipes
        - Creates harmonic, droning sounds
        - Central to Isan and Lao music culture
        """)
    
    st.subheader("🔬 Methodology")
    
    with st.expander("Feature Extraction"):
        st.markdown("""
        **Audio Features Analyzed:**
        
        1. **MFCCs (Mel-Frequency Cepstral Coefficients)**
           - Captures timbral characteristics
           - 20 coefficients with statistical measures (mean, std, max, min)
        
        2. **Chroma Features**
           - Represents pitch content
           - 12 chroma bins corresponding to musical notes
        
        3. **Spectral Features**
           - Spectral Centroid: Brightness of sound
           - Spectral Rolloff: Frequency distribution
           - Spectral Bandwidth: Range of frequencies
        
        4. **Temporal Features**
           - Zero-crossing rate
           - Tempo estimation
           - RMS energy
        
        5. **Pitch Features**
           - Fundamental frequency analysis
           - Pitch range and variability
        """)
    
    with st.expander("Machine Learning Model"):
        st.markdown("""
        **Model Architecture:**
        - Random Forest Classifier
        - 100 decision trees
        - Balanced class weights
        - Cross-validation for robustness
        
        **Training Process:**
        1. Audio preprocessing and normalization
        2. Feature extraction from audio segments
        3. Model training with validation split
        4. Cross-validation evaluation
        5. Performance metrics calculation
        """)
    
    with st.expander("Ethical Considerations"):
        st.markdown("""
        **Cultural Respect:**
        - All recordings require proper cultural attribution
        - Performer consent is tracked and required
        - Cultural context is preserved in metadata
        
        **Data Privacy:**
        - Performer information is protected
        - Consent status is validated
        - Transparent methodology for reproducibility
        
        **Academic Standards:**
        - Full documentation of data sources
        - Clear attribution of cultural origins
        - Reproducible research practices
        """)
    
    st.subheader("📊 Evaluation Metrics")
    st.markdown("""
    - **Accuracy**: Overall classification correctness
    - **Precision**: Reliability of positive predictions
    - **Recall**: Ability to find all positive cases
    - **F1-Score**: Harmonic mean of precision and recall
    - **Confusion Matrix**: Detailed classification breakdown
    - **Cross-Validation**: Multiple-fold validation for robustness
    """)

with tab4:
    st.header("About This Project")
    
    st.markdown("""
    ### Cultural Context
    
    This project aims to preserve and promote understanding of traditional Isan musical heritage 
    through modern AI technology. The Phin and Khaen are not just musical instruments—they are 
    integral parts of Northeastern Thai and Lao cultural identity.
    
    ### Technology Stack
    
    - **Audio Processing**: librosa, soundfile
    - **Machine Learning**: scikit-learn (Random Forest)
    - **Feature Engineering**: MFCC, Chroma, Spectral Analysis
    - **Web Interface**: Streamlit
    - **Visualization**: Plotly, Matplotlib, Seaborn
    
    ### Ethical Framework
    
    1. **Consent**: All recordings require documented performer consent
    2. **Attribution**: Proper cultural and performer attribution
    3. **Transparency**: Open methodology and reproducible research
    4. **Respect**: Maintaining cultural context and significance
    
    ### Future Development
    
    - Expand to more Isan instruments
    - Technique-specific classification
    - Regional variation analysis
    - Educational resources integration
    
    ### Contact & Contribution
    
    This is an open research project. We welcome contributions from:
    - Traditional musicians and cultural experts
    - Audio engineers and ML researchers
    - Cultural preservation organizations
    
    All contributions must follow our ethical guidelines and consent protocols.
    """)
    
    st.info("""
    **Note**: This is a demonstration system. For production use, ensure:
    - Proper consent documentation
    - Cultural expert consultation
    - Ethical review board approval
    - Community engagement and feedback
    """)

st.sidebar.markdown("---")
st.sidebar.markdown("""
**Version**: 1.0.0  
**Status**: Development  
**License**: Research & Educational Use
""")

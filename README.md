# Traditional Isan Musical Instruments Classifier

A machine learning system for recognizing and analyzing traditional Isan musical instruments: **Phin (พิณ)** and **Khaen (แคน)**.

## 🎯 Project Overview

This project combines audio machine learning with cultural preservation, creating an AI system that can:
- Classify traditional Isan instruments from audio recordings
- Analyze playing techniques and musical features
- Maintain ethical standards and cultural respect
- Support education and cultural preservation efforts

## 🎼 Instruments

### Phin (พิณ)
- Three-stringed lute from Northeastern Thailand
- Traditional instrument in Mor Lam performances
- Produces melodic, resonant tones

### Khaen (แคน)
- Bamboo mouth organ and national instrument of Laos
- Features multiple bamboo pipes
- Creates harmonic, droning sounds
- Central to Isan and Lao music culture

## 🚀 Quick Start

### 1. Installation

The required packages are already installed:
- librosa (audio processing)
- scikit-learn (machine learning)
- streamlit (web interface)
- And more...

### 2. Generate Demo Data

```bash
python examples/generate_demo_data.py
```

This creates synthetic audio samples for demonstration purposes.

### 3. Train the Model

```bash
python train_model.py
```

This will:
- Extract features from audio files
- Train a Random Forest classifier
- Evaluate model performance
- Save the trained model

### 4. Run the Web Application

```bash
streamlit run app.py
```

The application provides:
- Audio file upload and classification
- Real-time feature visualization
- Dataset management interface
- Comprehensive documentation

## 📁 Project Structure

```
.
├── src/
│   ├── preprocessing/
│   │   └── audio_processor.py      # Audio loading and preprocessing
│   ├── features/
│   │   └── feature_extractor.py    # Feature extraction (MFCC, chroma, etc.)
│   ├── models/
│   │   ├── classifier.py           # Random Forest classifier
│   │   └── dataset_manager.py      # Dataset metadata management
│   └── evaluation/
│       └── model_evaluator.py      # Model evaluation and visualization
├── data/
│   ├── raw/                        # Original audio recordings
│   ├── processed/                  # Preprocessed audio
│   └── metadata/                   # Dataset metadata (JSON)
├── models/                         # Trained models
├── docs/
│   ├── METHODOLOGY.md              # Technical methodology
│   └── DATA_COLLECTION_PROTOCOL.md # Ethical data collection guidelines
├── examples/
│   └── generate_demo_data.py       # Demo data generator
├── app.py                          # Streamlit web application
├── train_model.py                  # Model training pipeline
└── README.md                       # This file
```

## 🔬 Technical Approach

### Feature Extraction

The system extracts comprehensive audio features:

1. **MFCCs (Mel-Frequency Cepstral Coefficients)**
   - 20 coefficients with statistical measures
   - Captures timbral characteristics

2. **Chroma Features**
   - 12 chroma bins (musical notes)
   - Represents pitch content and harmony

3. **Spectral Features**
   - Spectral centroid (brightness)
   - Spectral rolloff (frequency distribution)
   - Spectral bandwidth (frequency range)

4. **Temporal Features**
   - Zero-crossing rate
   - Tempo estimation
   - RMS energy

5. **Pitch Features**
   - Fundamental frequency analysis
   - Pitch range and variability

### Machine Learning Model

- **Algorithm**: Random Forest Classifier
- **Features**: ~143 audio features per segment
- **Validation**: 5-fold cross-validation
- **Metrics**: Accuracy, Precision, Recall, F1-Score

### Audio Processing Pipeline

1. Load audio (22,050 Hz sample rate)
2. Normalize amplitude
3. Extract 3-second segments with overlap
4. Validate audio quality
5. Extract features
6. Classify instrument
7. Return confidence scores

## 📊 Web Application Features

### 🎵 Audio Classification
- Upload audio files (WAV, MP3, FLAC, OGG)
- Real-time instrument prediction
- Confidence scores and probability distributions
- Feature visualization

### 📈 Dataset Management
- Add new recordings with metadata
- Track consent and cultural attribution
- View dataset statistics
- Export dataset information

### 📚 Documentation
- Technical methodology
- Instrument information
- Ethical framework
- Evaluation metrics

## 🤝 Ethical Framework

This project prioritizes cultural respect and ethical AI development:

### Consent & Attribution
- Documented performer consent required
- Proper cultural attribution
- Transparent methodology
- Community engagement

### Cultural Respect
- Maintains cultural context
- Consults with cultural experts
- Supports traditional musicians
- Preserves intangible cultural heritage

### Data Privacy
- Secure metadata storage
- Protected performer information
- Controlled data access
- Optional anonymity

See `docs/DATA_COLLECTION_PROTOCOL.md` for complete guidelines.

## 📈 Model Performance

After training on the demo dataset, typical performance:
- **Accuracy**: 85-95% (depends on data quality)
- **Cross-validation**: Robust across different splits
- **Feature importance**: Identifies key discriminative features

*Note: Demo data is synthetic. Real-world performance depends on authentic recordings.*

## 🔮 Future Development

- Expand to additional Isan instruments
- Playing technique classification
- Regional variation analysis
- Mobile application
- Real-time classification
- Educational resources integration

## 📖 Documentation

Comprehensive documentation available in `docs/`:
- **METHODOLOGY.md**: Complete technical methodology
- **DATA_COLLECTION_PROTOCOL.md**: Ethical data collection guidelines

## ⚠️ Important Notes

### Demo Data
The included demo dataset uses synthetic audio for demonstration. For production use:
1. Collect authentic recordings from traditional musicians
2. Follow ethical data collection protocols
3. Obtain proper consent and attribution
4. Consult with cultural experts

### Cultural Sensitivity
This technology is intended for:
- Cultural preservation
- Educational purposes
- Research and analysis
- Supporting traditional musicians

It should NOT be used for:
- Commercial exploitation without consent
- Cultural appropriation
- Misrepresentation of traditions

## 🤝 Contributing

We welcome contributions from:
- Traditional musicians and cultural experts
- Audio engineers and ML researchers
- Cultural preservation organizations
- Educators and community members

All contributions must follow ethical guidelines and respect cultural protocols.

## 📝 License

This project is for research and educational use. Commercial use requires consultation with cultural communities and appropriate benefit sharing.

## 🙏 Acknowledgments

This project recognizes:
- Traditional Isan and Lao musicians
- Cultural preservation organizations
- Music schools and cultural institutions
- The communities who maintain these musical traditions

## 📧 Contact

For questions about:
- Cultural protocols and consultation
- Technical implementation
- Collaboration opportunities
- Educational partnerships

Please reach out through appropriate channels while respecting community protocols.

---

**Version**: 1.0.0  
**Status**: Development  
**Last Updated**: 2025-11-24

*Built with respect for traditional Isan musical heritage and commitment to ethical AI development.*

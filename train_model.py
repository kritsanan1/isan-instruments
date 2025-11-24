import numpy as np
import sys
from pathlib import Path
import json

sys.path.append(str(Path(__file__).parent))

from src.preprocessing.audio_processor import AudioProcessor
from src.features.feature_extractor import FeatureExtractor
from src.models.classifier import InstrumentClassifier
from src.models.dataset_manager import DatasetManager
from src.evaluation.model_evaluator import ModelEvaluator


def train_model_pipeline():
    print("=" * 60)
    print("Isan Musical Instruments Classification Training Pipeline")
    print("=" * 60)
    
    dataset_manager = DatasetManager()
    df = dataset_manager.export_to_dataframe()
    
    if df.empty:
        print("\n❌ Error: No recordings found in dataset!")
        print("Please add recordings using the dataset management interface.")
        return
    
    print(f"\n✓ Found {len(df)} recordings in dataset")
    
    consent_stats = dataset_manager.validate_consent()
    print(f"\n📝 Consent Status:")
    print(f"  - With consent: {consent_stats['with_consent']}")
    print(f"  - Without consent: {consent_stats['without_consent']}")
    print(f"  - Consent rate: {consent_stats['consent_rate']*100:.1f}%")
    
    if consent_stats['consent_rate'] < 1.0:
        print("\n⚠️  Warning: Not all recordings have documented consent!")
        response = input("Continue anyway? (yes/no): ")
        if response.lower() != 'yes':
            print("Training cancelled.")
            return
    
    print("\n" + "=" * 60)
    print("Feature Extraction")
    print("=" * 60)
    
    processor = AudioProcessor(target_sr=22050)
    extractor = FeatureExtractor(sr=22050)
    
    features_list = []
    labels_list = []
    
    for idx, row in df.iterrows():
        file_path = row['file_path']
        instrument = row['instrument']
        
        print(f"\n[{idx+1}/{len(df)}] Processing: {Path(file_path).name}")
        print(f"  Instrument: {instrument}")
        
        try:
            if not Path(file_path).exists():
                print(f"  ⚠️  File not found, skipping...")
                continue
            
            audio, sr, quality = processor.preprocess_audio(file_path)
            
            if not quality['is_valid']:
                print(f"  ⚠️  Quality check failed: {quality.get('reason', 'Unknown')}")
                continue
            
            segments = processor.extract_segments(audio, sr, segment_duration=3.0)
            print(f"  ✓ Extracted {len(segments)} segments")
            
            for seg_idx, segment in enumerate(segments):
                features = extractor.extract_all_features(segment)
                features_list.append(features)
                labels_list.append(instrument)
            
            print(f"  ✓ Features extracted successfully")
            
        except Exception as e:
            print(f"  ❌ Error: {str(e)}")
            continue
    
    if len(features_list) == 0:
        print("\n❌ Error: No valid features extracted!")
        return
    
    X = np.array(features_list)
    y = np.array(labels_list)
    
    print(f"\n✓ Total feature vectors: {len(X)}")
    print(f"✓ Feature dimension: {X.shape[1]}")
    print(f"✓ Class distribution:")
    for instrument in np.unique(y):
        count = np.sum(y == instrument)
        print(f"  - {instrument}: {count} samples ({count/len(y)*100:.1f}%)")
    
    print("\n" + "=" * 60)
    print("Model Training")
    print("=" * 60)
    
    classifier = InstrumentClassifier(n_estimators=100, random_state=42)
    
    print("\nTraining Random Forest classifier...")
    results = classifier.train(X, y, validation_split=0.2)
    
    print("\n📊 Training Results:")
    print(f"  - Training Accuracy: {results['train_accuracy']*100:.2f}%")
    print(f"  - Validation Accuracy: {results['validation_accuracy']*100:.2f}%")
    print(f"  - Cross-Validation Mean: {results['cv_mean']*100:.2f}%")
    print(f"  - Cross-Validation Std: {results['cv_std']*100:.2f}%")
    
    print("\n📈 Per-Class Performance:")
    for class_name in classifier.label_encoder.classes_:
        if class_name in results['classification_report']:
            metrics = results['classification_report'][class_name]
            print(f"\n  {class_name}:")
            print(f"    Precision: {metrics['precision']:.4f}")
            print(f"    Recall: {metrics['recall']:.4f}")
            print(f"    F1-Score: {metrics['f1-score']:.4f}")
    
    print("\n" + "=" * 60)
    print("Model Evaluation & Export")
    print("=" * 60)
    
    evaluator = ModelEvaluator()
    
    feature_names = extractor.get_feature_names()
    importance = classifier.get_feature_importance(feature_names, top_n=20)
    
    print("\n🔍 Top 10 Most Important Features:")
    for i, (feature, imp) in enumerate(list(importance.items())[:10], 1):
        print(f"  {i}. {feature}: {imp:.4f}")
    
    models_dir = Path("models")
    models_dir.mkdir(exist_ok=True)
    
    model_path = models_dir / "instrument_classifier.pkl"
    classifier.save_model(str(model_path))
    print(f"\n✓ Model saved to: {model_path}")
    
    results_path = models_dir / "training_results.json"
    with open(results_path, 'w') as f:
        json.dump(results, f, indent=2)
    print(f"✓ Results saved to: {results_path}")
    
    print("\n" + "=" * 60)
    print("Training Complete!")
    print("=" * 60)
    print("\nYou can now use the Streamlit app to classify new audio files.")
    print("Run: streamlit run app.py")


if __name__ == "__main__":
    train_model_pipeline()

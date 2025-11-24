# Traditional Isan Musical Instruments Classifier

## Overview

This project is a machine learning system designed to recognize and classify traditional Isan musical instruments from audio recordings. Specifically, it focuses on two instruments: the **Phin (พิณ)** - a three-stringed lute from Northeastern Thailand, and the **Khaen (แคน)** - a bamboo mouth organ and national instrument of Laos.

The system combines audio signal processing, feature extraction, and machine learning classification with a strong emphasis on cultural preservation and ethical AI practices. It includes capabilities for audio preprocessing, feature engineering, model training/evaluation, and an interactive web interface for real-time classification.

The project serves both educational and cultural preservation purposes, enabling researchers, musicians, and enthusiasts to understand and document these traditional instruments through modern AI technology.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Audio Processing Pipeline

**Problem**: Raw audio files need to be standardized and prepared for feature extraction.

**Solution**: The `AudioProcessor` class handles audio loading, normalization, and segmentation with a target sample rate of 22,050 Hz.

**Design Rationale**: 
- Uses librosa for robust audio file handling across formats
- Normalizes amplitude to prevent scale-related classification issues
- Implements overlapping segmentation (3-second windows with 50% overlap) to generate multiple training samples from longer recordings
- Validates audio quality through metrics (duration, amplitude, RMS energy) before processing

### Feature Extraction Architecture

**Problem**: Machine learning models need numerical representations of audio characteristics that distinguish between instruments.

**Solution**: The `FeatureExtractor` class extracts multiple audio feature sets including MFCCs (Mel-frequency cepstral coefficients), chroma features, spectral characteristics, and temporal features.

**Design Rationale**:
- MFCCs capture timbral characteristics (20 coefficients with statistical aggregations: mean, std, max, min)
- Chroma features represent harmonic content, crucial for distinguishing melodic (Phin) vs. harmonic (Khaen) instruments
- Spectral features (centroid, rolloff, bandwidth) capture frequency distribution differences
- Temporal features (zero-crossing rate, RMS energy) help identify playing technique patterns
- Statistical aggregations over time reduce dimensionality while preserving essential information

### Classification Model

**Problem**: Need a robust classifier that works well with limited training data and provides interpretable results.

**Solution**: Random Forest classifier with 100 estimators, balanced class weights, and controlled tree depth.

**Design Rationale**:
- Random Forest chosen for robustness with small datasets and built-in feature importance
- Class balancing addresses potential data imbalance between instruments
- Hyperparameters (max_depth=20, min_samples_split=5) prevent overfitting
- Includes cross-validation (5-fold) for reliable performance estimation
- LabelEncoder handles string labels for instrument types

### Dataset Management System

**Problem**: Need structured storage of audio metadata, consent documentation, and cultural attribution for ethical AI development.

**Solution**: The `DatasetManager` class maintains a JSON-based metadata system tracking recordings, performer consent, cultural attribution, and playing techniques.

**Design Rationale**:
- JSON format for human-readable, version-controllable metadata
- Each recording includes: file path, instrument type, technique, performer info, consent status, cultural attribution, timestamps
- Validation methods ensure consent compliance before model training
- DataFrame export capability for analysis and reporting
- Structured around ethical AI principles with explicit consent tracking

### Web Interface Architecture

**Problem**: Users need an accessible way to interact with the classification system without coding knowledge.

**Solution**: Streamlit-based web application with multiple tabs for classification, dataset management, model information, and visualization.

**Design Rationale**:
- Streamlit chosen for rapid development and built-in UI components
- Tab-based organization separates concerns (classification, data management, training, visualization)
- Caching decorator (`@st.cache_resource`) loads models once to improve performance
- File upload handling with temporary storage for audio processing
- Interactive visualizations using Plotly for confusion matrices and feature importance

**Architecture Components**:
1. **Classification Tab**: Upload audio → process → extract features → predict → display results
2. **Dataset Management Tab**: Add recordings with metadata and consent documentation
3. **Model Information Tab**: Display performance metrics and evaluation results
4. **Visualization Tab**: Interactive plots of model behavior and feature analysis

### Training Pipeline

**Problem**: Need reproducible, auditable model training with ethical safeguards.

**Solution**: The `train_model.py` script implements a complete pipeline: consent validation → feature extraction → model training → evaluation → persistence.

**Design Rationale**:
- Validates consent status before training, with user confirmation if consent rate < 100%
- Extracts features from all recordings in dataset
- Trains model with validation split and cross-validation
- Generates evaluation metrics (accuracy, confusion matrix, classification report)
- Saves trained model and metadata for reproducibility
- Progress reporting for transparency

### Evaluation Framework

**Problem**: Need comprehensive assessment of model performance with interpretable metrics.

**Solution**: The `ModelEvaluator` class generates confusion matrices, classification reports, and feature importance visualizations.

**Design Rationale**:
- Confusion matrix reveals classification patterns and common errors
- Per-class metrics (precision, recall, F1) identify instrument-specific performance
- Feature importance plots highlight which audio characteristics drive classification
- Matplotlib/Seaborn for publication-quality visualizations
- Results stored as JSON for reproducibility and reporting

### Data Generation for Development

**Problem**: Need synthetic data for development and demonstration when real recordings aren't available.

**Solution**: The `generate_demo_data.py` script creates synthetic audio samples with instrument-specific characteristics.

**Design Rationale**:
- Phin simulation: fundamental + harmonics with plucked envelope and vibrato
- Khaen simulation: multiple harmonics with tremolo to mimic breath-driven sound
- Adds realistic noise for robustness
- Creates multiple samples per instrument for model training
- Clearly marked as synthetic in metadata for ethical transparency

## External Dependencies

### Audio Processing Libraries
- **librosa**: Core audio analysis library for loading, resampling, and feature extraction
- **soundfile**: Audio file I/O operations

### Machine Learning Stack
- **scikit-learn**: Random Forest classifier, preprocessing, evaluation metrics, cross-validation
- **numpy**: Numerical operations and array handling throughout the pipeline

### Web Application
- **streamlit**: Web interface framework for the interactive classifier application
- **plotly**: Interactive visualizations for confusion matrices and feature plots
- **pandas**: Data manipulation and dataset export to DataFrame format

### Visualization
- **matplotlib**: Static plot generation for evaluation reports
- **seaborn**: Enhanced statistical visualizations, particularly for confusion matrices

### Utilities
- **joblib**: Model serialization and persistence
- **json**: Metadata storage and configuration management
- **pathlib**: Cross-platform file path handling

### File Format Support
The system handles various audio formats through librosa (WAV, MP3, FLAC, OGG) with automatic resampling to 22,050 Hz target sample rate.

### Data Storage
- **Metadata**: JSON files in `data/metadata/` directory
- **Audio Files**: Raw recordings in `data/raw/` directory (organized by instrument)
- **Models**: Serialized classifiers in `models/` directory using joblib pickle format
- **Evaluation**: Plots and metrics stored as PNG/JSON in evaluation outputs
# Methodology: Isan Musical Instruments Classification

## 1. Introduction

This document outlines the comprehensive methodology for developing a machine learning system to recognize and analyze traditional Isan musical instruments, specifically the Phin (พิณ) and Khaen (แคน).

## 2. Cultural Context

### 2.1 Instruments

**Phin (พิณ)**
- Three-stringed lute from Northeastern Thailand
- Integral to Mor Lam traditional music performances
- Produces melodic, resonant tones with distinctive timbral characteristics
- Typically made from wood with a long neck and small resonating chamber

**Khaen (แคน)**
- Bamboo mouth organ and national instrument of Laos
- Features multiple bamboo pipes arranged in parallel
- Creates harmonic, droning sounds with unique overtone patterns
- Central to Isan and Lao musical traditions

### 2.2 Cultural Significance

Both instruments represent centuries of musical tradition and are essential to:
- Traditional ceremonies and celebrations
- Storytelling through Mor Lam performances
- Cultural identity of Isan and Lao communities
- Preservation of intangible cultural heritage

## 3. Ethical Framework

### 3.1 Data Collection Ethics

**Consent Protocol:**
- Explicit informed consent required from all performers
- Documentation of consent status in metadata
- Right to withdraw consent at any time
- Clear explanation of AI research purposes

**Cultural Attribution:**
- Proper attribution to performers and cultural sources
- Documentation of regional variations and styles
- Consultation with cultural experts and traditional musicians
- Recognition of community knowledge ownership

### 3.2 Ethical AI Development

**Transparency:**
- Open methodology and reproducible research
- Clear documentation of limitations
- Public availability of technical approach

**Respect:**
- Maintaining cultural context in all documentation
- Avoiding cultural appropriation or misrepresentation
- Centering community voices and perspectives

**Responsibility:**
- Ensuring technology serves cultural preservation
- Preventing commercial exploitation
- Supporting traditional musicians and cultural practitioners

## 4. Technical Methodology

### 4.1 Audio Preprocessing Pipeline

**Step 1: Audio Loading**
- Target sample rate: 22,050 Hz (standard for music analysis)
- Automatic resampling if needed
- Support for multiple audio formats (WAV, MP3, FLAC, OGG)

**Step 2: Normalization**
- Amplitude normalization to [-1, 1] range
- Preserves relative dynamics while ensuring consistent processing

**Step 3: Segmentation**
- 3-second segments with 50% overlap
- Captures both short-term and longer-term patterns
- Increases training data through augmentation

**Step 4: Quality Validation**
- Minimum duration check (>0.5 seconds)
- Amplitude validation (not too quiet)
- Signal-to-noise ratio assessment
- Zero-crossing rate verification

### 4.2 Feature Extraction

**MFCCs (Mel-Frequency Cepstral Coefficients)**
- 20 coefficients extracted
- Statistical measures: mean, std, max, min (80 features)
- Captures timbral characteristics unique to each instrument
- Based on human auditory perception model

**Chroma Features**
- 12 chroma bins (musical notes)
- Statistical measures: mean, std, max, min (48 features)
- Represents pitch content and harmonic structure
- Distinguishes melodic patterns

**Spectral Features**
- Spectral Centroid: Brightness/center of mass of spectrum
- Spectral Rolloff: Frequency below which 85% of energy is contained
- Spectral Bandwidth: Width of frequency distribution
- Statistical measures for temporal variation (6 features)

**Temporal Features**
- Zero-Crossing Rate: Indicates pitch and percussiveness
- Tempo: Estimated beats per minute
- RMS Energy: Overall loudness and dynamics
- Statistical measures (5 features)

**Pitch Features**
- Fundamental frequency extraction
- Pitch range and variability
- Statistical measures: mean, std, max, min (4 features)

**Total Feature Vector Dimension: ~143 features**

### 4.3 Machine Learning Model

**Architecture: Random Forest Classifier**

*Rationale:*
- Handles high-dimensional feature spaces well
- Robust to overfitting through ensemble approach
- Provides feature importance rankings
- No need for feature scaling
- Interpretable decision boundaries

*Hyperparameters:*
- Number of estimators: 100 trees
- Max depth: 20 (prevents overfitting)
- Min samples split: 5
- Min samples leaf: 2
- Class weight: balanced (handles class imbalance)
- Random state: 42 (reproducibility)

*Training Process:*
1. 80/20 train-validation split
2. Stratified sampling to preserve class distribution
3. 5-fold cross-validation for robust evaluation
4. Feature importance analysis

### 4.4 Evaluation Metrics

**Primary Metrics:**
- Accuracy: Overall classification correctness
- Precision: Reliability of positive predictions per class
- Recall: Ability to find all instances of each class
- F1-Score: Harmonic mean of precision and recall

**Additional Analysis:**
- Confusion Matrix: Detailed error analysis
- Cross-Validation Scores: Robustness across data splits
- Feature Importance: Understanding model decisions
- Confidence Scores: Prediction reliability

**Validation Strategy:**
- 5-fold cross-validation
- Stratified sampling
- Independent test set evaluation
- Performance across different recording conditions

## 5. Dataset Management

### 5.1 Metadata Schema

```json
{
  "recording_id": "Unique identifier",
  "file_path": "Path to audio file",
  "instrument_type": "Phin or Khaen",
  "playing_technique": "Specific technique used",
  "performer": {
    "name": "Performer name",
    "consent_obtained": true/false
  },
  "cultural_attribution": "Cultural source and context",
  "added_at": "ISO timestamp",
  "notes": "Additional information"
}
```

### 5.2 Data Organization

```
data/
├── raw/              # Original audio recordings
├── processed/        # Preprocessed audio
└── metadata/         # JSON metadata files
    └── dataset_metadata.json
```

### 5.3 Quality Control

- Audio quality validation
- Consent verification
- Cultural attribution completeness
- Regular dataset audits
- Performer information protection

## 6. Implementation Details

### 6.1 Technology Stack

**Core Libraries:**
- librosa: Audio analysis and feature extraction
- scikit-learn: Machine learning and evaluation
- numpy: Numerical computing
- pandas: Data management

**Interface:**
- Streamlit: Interactive web application
- plotly: Interactive visualizations
- matplotlib/seaborn: Static plots

### 6.2 Reproducibility

**Random Seeds:**
- Random state: 42 for all random operations
- Ensures consistent results across runs

**Version Control:**
- All code versioned with git
- Dependencies specified in requirements.txt
- Documentation of all parameters

**Environment:**
- Python 3.11+
- Specific library versions documented
- System requirements specified

## 7. Limitations and Future Work

### 7.1 Current Limitations

- Binary classification (Phin vs Khaen only)
- Requires clean audio recordings
- Limited to available playing techniques
- Dependent on training data quality and diversity

### 7.2 Future Enhancements

**Multi-class Extension:**
- Add more Isan instruments (Pin Pia, Saw, etc.)
- Regional variation classification
- Performer style recognition

**Technique Classification:**
- Specific playing technique identification
- Articulation analysis
- Performance style categorization

**Advanced Features:**
- Deep learning approaches (CNNs on spectrograms)
- Transfer learning from pre-trained models
- Real-time classification
- Mobile application deployment

**Cultural Integration:**
- Educational resources development
- Collaboration with music schools
- Traditional musician training programs
- Cultural preservation initiatives

## 8. Conclusion

This methodology balances technical rigor with cultural sensitivity, ensuring that AI technology serves to preserve and promote traditional Isan musical heritage while respecting the cultural significance and community ownership of this knowledge.

## 9. References and Resources

**Cultural Resources:**
- Collaboration with traditional music experts
- Cultural heritage organizations
- Music schools in Isan region
- Academic ethnomusicology research

**Technical Resources:**
- librosa documentation
- scikit-learn documentation
- Audio signal processing literature
- Music information retrieval research

## 10. Version History

- Version 1.0.0 (2025-11-24): Initial methodology documentation

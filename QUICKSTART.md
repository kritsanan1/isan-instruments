# Quick Start Guide

## Get Started in 3 Steps

### Step 1: Generate Demo Data

Run this command to create synthetic audio samples:

```bash
python examples/generate_demo_data.py
```

This creates 6 audio files (3 Phin, 3 Khaen) and adds them to the dataset with proper metadata.

### Step 2: Train the Model

Run the training pipeline:

```bash
python train_model.py
```

This will:
- Extract features from all audio files
- Train a Random Forest classifier
- Evaluate performance with cross-validation
- Save the trained model to `models/instrument_classifier.pkl`

Expected output:
- Training accuracy: ~90-95%
- Validation accuracy: ~85-95%
- Feature importance rankings

### Step 3: Use the Web App

The Streamlit application is already running! Use it to:

1. **Classify Audio**: Upload any audio file to get predictions
2. **Manage Dataset**: Add new recordings with metadata
3. **View Documentation**: Learn about the methodology
4. **Explore Features**: Visualize audio characteristics

## What's Next?

### For Research
- Replace synthetic data with real recordings
- Follow ethical data collection protocols (see `docs/DATA_COLLECTION_PROTOCOL.md`)
- Collect performer consent
- Document cultural attribution

### For Development
- Add more instruments
- Implement technique classification
- Improve feature extraction
- Expand evaluation metrics

### For Production
- Collect authentic recordings from traditional musicians
- Consult with cultural experts
- Implement additional validation
- Add more robust error handling

## Need Help?

- **Technical Details**: See `docs/METHODOLOGY.md`
- **Ethical Guidelines**: See `docs/DATA_COLLECTION_PROTOCOL.md`
- **Full Documentation**: See `README.md`

## Important Notes

⚠️ The demo data is synthetic and for demonstration only. For real-world use, you need authentic recordings of Phin and Khaen from traditional musicians with proper consent and cultural attribution.

🤝 This project prioritizes cultural respect and ethical AI development. Always follow the ethical guidelines when collecting real data.

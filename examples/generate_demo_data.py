import numpy as np
import soundfile as sf
from pathlib import Path
import sys

sys.path.append(str(Path(__file__).parent.parent))

from src.models.dataset_manager import DatasetManager


def generate_synthetic_audio(instrument_type: str, duration: float = 5.0, sr: int = 22050):
    t = np.linspace(0, duration, int(sr * duration))
    
    if instrument_type == "Phin":
        base_freq = 220
        fundamental = np.sin(2 * np.pi * base_freq * t)
        harmonic2 = 0.5 * np.sin(2 * np.pi * base_freq * 2 * t)
        harmonic3 = 0.3 * np.sin(2 * np.pi * base_freq * 3 * t)
        
        envelope = np.exp(-2 * t)
        modulation = 1 + 0.3 * np.sin(2 * np.pi * 5 * t)
        
        audio = (fundamental + harmonic2 + harmonic3) * envelope * modulation
        
    else:
        base_freq = 165
        harmonics = []
        for i in range(1, 6):
            amp = 1.0 / i
            freq = base_freq * i
            harmonics.append(amp * np.sin(2 * np.pi * freq * t))
        
        drone = sum(harmonics)
        
        tremolo = 1 + 0.4 * np.sin(2 * np.pi * 6 * t)
        audio = drone * tremolo
    
    audio = audio / np.max(np.abs(audio)) * 0.8
    
    noise = np.random.randn(len(audio)) * 0.02
    audio = audio + noise
    
    return audio, sr


def create_demo_dataset():
    print("Creating demonstration dataset...")
    print("=" * 60)
    
    data_dir = Path("data/raw")
    data_dir.mkdir(parents=True, exist_ok=True)
    
    dataset_manager = DatasetManager()
    
    instruments = [
        ("Phin", "Traditional Melody", "Somchai Isan", "Northeastern Thailand (Isan Region)"),
        ("Phin", "Fingerpicking Style", "Nittaya Kham", "Udon Thani Province, Thailand"),
        ("Phin", "Slow Ballad", "Somchai Isan", "Northeastern Thailand (Isan Region)"),
        ("Khaen", "Drone Pattern", "Bounmy Laos", "Vientiane, Laos"),
        ("Khaen", "Fast Rhythm", "Souk Siphan", "Savannakhet, Laos"),
        ("Khaen", "Traditional Lam", "Bounmy Laos", "Vientiane, Laos"),
    ]
    
    for idx, (instrument, technique, performer, region) in enumerate(instruments, 1):
        print(f"\n[{idx}/{len(instruments)}] Generating {instrument} - {technique}")
        
        audio, sr = generate_synthetic_audio(instrument, duration=6.0, sr=22050)
        
        filename = f"{instrument.lower()}_{technique.replace(' ', '_').lower()}_{idx}.wav"
        filepath = data_dir / filename
        
        sf.write(filepath, audio, sr)
        print(f"  ✓ Saved to: {filepath}")
        
        recording_id = dataset_manager.add_recording(
            file_path=str(filepath),
            instrument=instrument,
            technique=technique,
            performer_name=performer,
            consent_status=True,
            cultural_attribution=region,
            notes=f"Synthetic demonstration audio for {instrument} - {technique}"
        )
        
        print(f"  ✓ Added to dataset with ID: {recording_id}")
    
    print("\n" + "=" * 60)
    print("Demo Dataset Creation Complete!")
    print("=" * 60)
    
    df = dataset_manager.export_to_dataframe()
    print(f"\nTotal recordings: {len(df)}")
    print(f"\nInstrument distribution:")
    print(df['instrument'].value_counts())
    
    print("\n⚠️  IMPORTANT NOTE:")
    print("These are synthetic audio files for demonstration purposes only.")
    print("For real-world use, replace with actual recordings of Phin and Khaen")
    print("following the ethical data collection protocols in docs/")
    
    print("\nNext steps:")
    print("1. Run: python train_model.py")
    print("2. Run: streamlit run app.py")


if __name__ == "__main__":
    create_demo_dataset()

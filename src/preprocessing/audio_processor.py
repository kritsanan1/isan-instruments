import numpy as np
import librosa
import soundfile as sf
from pathlib import Path
from typing import Tuple, Optional
import warnings

warnings.filterwarnings('ignore')


class AudioProcessor:
    def __init__(self, target_sr: int = 22050, duration: Optional[float] = None):
        self.target_sr = target_sr
        self.duration = duration
    
    def load_audio(self, file_path: str) -> Tuple[np.ndarray, int]:
        try:
            audio, sr = librosa.load(file_path, sr=self.target_sr, duration=self.duration)
            return audio, int(sr)
        except Exception as e:
            raise ValueError(f"Error loading audio file {file_path}: {str(e)}")
    
    def normalize_audio(self, audio: np.ndarray) -> np.ndarray:
        if np.max(np.abs(audio)) > 0:
            return audio / np.max(np.abs(audio))
        return audio
    
    def extract_segments(self, audio: np.ndarray, sr: int, segment_duration: float = 3.0, 
                        overlap: float = 0.5) -> list:
        segment_samples = int(segment_duration * sr)
        hop_samples = int(segment_samples * (1 - overlap))
        
        segments = []
        start = 0
        
        while start + segment_samples <= len(audio):
            segment = audio[start:start + segment_samples]
            segments.append(segment)
            start += hop_samples
        
        if len(segments) == 0 and len(audio) > 0:
            segments.append(audio)
        
        return segments
    
    def validate_audio_quality(self, audio: np.ndarray, sr: int) -> dict:
        quality_metrics = {
            'duration': len(audio) / sr,
            'max_amplitude': float(np.max(np.abs(audio))),
            'rms_energy': float(np.sqrt(np.mean(audio**2))),
            'zero_crossing_rate': float(np.mean(librosa.zero_crossings(audio))),
            'is_valid': True
        }
        
        if quality_metrics['duration'] < 0.5:
            quality_metrics['is_valid'] = False
            quality_metrics['reason'] = 'Audio too short'
        elif quality_metrics['max_amplitude'] < 0.01:
            quality_metrics['is_valid'] = False
            quality_metrics['reason'] = 'Audio too quiet'
        
        return quality_metrics
    
    def preprocess_audio(self, file_path: str) -> Tuple[np.ndarray, int, dict]:
        audio, sr = self.load_audio(file_path)
        audio = self.normalize_audio(audio)
        quality = self.validate_audio_quality(audio, sr)
        
        return audio, sr, quality

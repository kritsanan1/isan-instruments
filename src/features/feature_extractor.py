import numpy as np
import librosa
from typing import Dict
import warnings

warnings.filterwarnings('ignore')


class FeatureExtractor:
    def __init__(self, sr: int = 22050):
        self.sr = sr
    
    def extract_mfcc_features(self, audio: np.ndarray, n_mfcc: int = 20) -> Dict[str, np.ndarray]:
        mfccs = librosa.feature.mfcc(y=audio, sr=self.sr, n_mfcc=n_mfcc)
        
        return {
            'mfcc_mean': np.mean(mfccs, axis=1),
            'mfcc_std': np.std(mfccs, axis=1),
            'mfcc_max': np.max(mfccs, axis=1),
            'mfcc_min': np.min(mfccs, axis=1)
        }
    
    def extract_chroma_features(self, audio: np.ndarray) -> Dict[str, np.ndarray]:
        chroma = librosa.feature.chroma_stft(y=audio, sr=self.sr)
        
        return {
            'chroma_mean': np.mean(chroma, axis=1),
            'chroma_std': np.std(chroma, axis=1),
            'chroma_max': np.max(chroma, axis=1),
            'chroma_min': np.min(chroma, axis=1)
        }
    
    def extract_spectral_features(self, audio: np.ndarray) -> Dict[str, float]:
        spectral_centroids = librosa.feature.spectral_centroid(y=audio, sr=self.sr)[0]
        spectral_rolloff = librosa.feature.spectral_rolloff(y=audio, sr=self.sr)[0]
        spectral_bandwidth = librosa.feature.spectral_bandwidth(y=audio, sr=self.sr)[0]
        
        return {
            'spectral_centroid_mean': float(np.mean(spectral_centroids)),
            'spectral_centroid_std': float(np.std(spectral_centroids)),
            'spectral_rolloff_mean': float(np.mean(spectral_rolloff)),
            'spectral_rolloff_std': float(np.std(spectral_rolloff)),
            'spectral_bandwidth_mean': float(np.mean(spectral_bandwidth)),
            'spectral_bandwidth_std': float(np.std(spectral_bandwidth))
        }
    
    def extract_temporal_features(self, audio: np.ndarray) -> Dict[str, float]:
        zero_crossings = librosa.zero_crossings(audio)
        zcr = np.sum(zero_crossings)
        
        onset_env = librosa.onset.onset_strength(y=audio, sr=self.sr)
        tempo, _ = librosa.beat.beat_track(onset_envelope=onset_env, sr=self.sr)
        
        rms = librosa.feature.rms(y=audio)[0]
        
        return {
            'zero_crossing_rate': float(zcr / len(audio)),
            'tempo': float(tempo),
            'rms_mean': float(np.mean(rms)),
            'rms_std': float(np.std(rms)),
            'rms_max': float(np.max(rms))
        }
    
    def extract_pitch_features(self, audio: np.ndarray) -> Dict[str, float]:
        pitches, magnitudes = librosa.piptrack(y=audio, sr=self.sr)
        
        pitch_values = []
        for t in range(pitches.shape[1]):
            index = magnitudes[:, t].argmax()
            pitch = pitches[index, t]
            if pitch > 0:
                pitch_values.append(pitch)
        
        if len(pitch_values) > 0:
            return {
                'pitch_mean': float(np.mean(pitch_values)),
                'pitch_std': float(np.std(pitch_values)),
                'pitch_max': float(np.max(pitch_values)),
                'pitch_min': float(np.min(pitch_values))
            }
        else:
            return {
                'pitch_mean': 0.0,
                'pitch_std': 0.0,
                'pitch_max': 0.0,
                'pitch_min': 0.0
            }
    
    def extract_all_features(self, audio: np.ndarray) -> np.ndarray:
        feature_dict = {}
        
        mfcc = self.extract_mfcc_features(audio)
        chroma = self.extract_chroma_features(audio)
        spectral = self.extract_spectral_features(audio)
        temporal = self.extract_temporal_features(audio)
        pitch = self.extract_pitch_features(audio)
        
        feature_dict.update(mfcc)
        feature_dict.update(chroma)
        feature_dict.update(spectral)
        feature_dict.update(temporal)
        feature_dict.update(pitch)
        
        features = []
        for key in sorted(feature_dict.keys()):
            value = feature_dict[key]
            if isinstance(value, np.ndarray):
                features.extend(value.tolist())
            else:
                features.append(value)
        
        return np.array(features)
    
    def get_feature_names(self) -> list:
        dummy_audio = np.random.randn(self.sr * 3)
        feature_dict = {}
        
        mfcc = self.extract_mfcc_features(dummy_audio)
        chroma = self.extract_chroma_features(dummy_audio)
        spectral = self.extract_spectral_features(dummy_audio)
        temporal = self.extract_temporal_features(dummy_audio)
        pitch = self.extract_pitch_features(dummy_audio)
        
        feature_dict.update(mfcc)
        feature_dict.update(chroma)
        feature_dict.update(spectral)
        feature_dict.update(temporal)
        feature_dict.update(pitch)
        
        feature_names = []
        for key in sorted(feature_dict.keys()):
            value = feature_dict[key]
            if isinstance(value, np.ndarray):
                for i in range(len(value)):
                    feature_names.append(f"{key}_{i}")
            else:
                feature_names.append(key)
        
        return feature_names

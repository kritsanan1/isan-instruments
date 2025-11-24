import numpy as np
import librosa
from typing import List, Tuple
from scipy.signal import find_peaks


class OnsetDetector:
    """
    Onset detection using EWMA (Exponentially Weighted Moving Average) approach
    Based on KMUTT research: achieved 98.54% F1-score for Thai instruments
    """
    
    def __init__(self, sr: int = 22050, hop_length: int = 512):
        self.sr = sr
        self.hop_length = hop_length
        self.frame_time = hop_length / sr
    
    def compute_energy(self, audio: np.ndarray) -> np.ndarray:
        """Compute frame-wise energy using RMS"""
        energy = librosa.feature.rms(y=audio, hop_length=self.hop_length)[0]
        return energy
    
    def ewma_filter(self, signal: np.ndarray, alpha: float = 0.3) -> np.ndarray:
        """Apply Exponentially Weighted Moving Average filter"""
        filtered = np.zeros_like(signal)
        filtered[0] = signal[0]
        
        for i in range(1, len(signal)):
            filtered[i] = alpha * signal[i] + (1 - alpha) * filtered[i-1]
        
        return filtered
    
    def detect_onsets(self, audio: np.ndarray, 
                      threshold_ratio: float = 1.5,
                      min_duration: float = 0.05) -> np.ndarray:
        """
        Detect note onsets using energy-based method with EWMA
        
        Args:
            audio: Audio signal
            threshold_ratio: Multiplier for dynamic threshold
            min_duration: Minimum time between onsets (seconds)
        
        Returns:
            Array of onset times in seconds
        """
        energy = self.compute_energy(audio)
        
        ewma = self.ewma_filter(energy, alpha=0.3)
        
        threshold = ewma * threshold_ratio
        
        onset_frames = []
        for i in range(1, len(energy)):
            if energy[i] > threshold[i] and energy[i] > energy[i-1]:
                onset_frames.append(i)
        
        onset_times = librosa.frames_to_time(
            onset_frames, 
            sr=self.sr, 
            hop_length=self.hop_length
        )
        
        min_samples = int(min_duration / self.frame_time)
        filtered_onsets = []
        last_onset = -min_samples
        
        for onset in onset_frames:
            if onset - last_onset >= min_samples:
                filtered_onsets.append(onset)
                last_onset = onset
        
        onset_times = librosa.frames_to_time(
            filtered_onsets,
            sr=self.sr,
            hop_length=self.hop_length
        )
        
        return onset_times
    
    def detect_onsets_with_librosa(self, audio: np.ndarray) -> np.ndarray:
        """Alternative onset detection using librosa's built-in method"""
        onset_env = librosa.onset.onset_strength(y=audio, sr=self.sr)
        onset_frames = librosa.onset.onset_detect(
            onset_envelope=onset_env,
            sr=self.sr,
            hop_length=self.hop_length
        )
        onset_times = librosa.frames_to_time(
            onset_frames,
            sr=self.sr,
            hop_length=self.hop_length
        )
        return onset_times
    
    def get_note_durations(self, onset_times: np.ndarray, 
                          audio_duration: float) -> np.ndarray:
        """Calculate duration of each note based on onset times"""
        if len(onset_times) == 0:
            return np.array([])
        
        durations = np.diff(onset_times)
        last_duration = audio_duration - onset_times[-1]
        durations = np.append(durations, last_duration)
        
        return durations

import numpy as np
import librosa
from typing import List, Tuple, Optional
from scipy.signal import find_peaks


class PitchDetector:
    """
    Pitch detection using FFT and peak detection
    Based on KMUTT research: achieved 97.34% F1-score for Thai instruments
    """
    
    def __init__(self, sr: int = 22050, hop_length: int = 512):
        self.sr = sr
        self.hop_length = hop_length
        self.fmin = librosa.note_to_hz('C2')
        self.fmax = librosa.note_to_hz('C7')
    
    def detect_pitch_fft(self, audio_segment: np.ndarray) -> Tuple[float, float]:
        """
        Detect pitch using FFT-based method
        
        Returns:
            (frequency_hz, confidence)
        """
        fft = np.fft.fft(audio_segment)
        magnitude = np.abs(fft[:len(fft)//2])
        freqs = np.fft.fftfreq(len(audio_segment), 1/self.sr)[:len(fft)//2]
        
        valid_idx = np.where((freqs >= self.fmin) & (freqs <= self.fmax))[0]
        
        if len(valid_idx) == 0:
            return 0.0, 0.0
        
        valid_freqs = freqs[valid_idx]
        valid_mag = magnitude[valid_idx]
        
        peaks, properties = find_peaks(valid_mag, height=np.max(valid_mag) * 0.3)
        
        if len(peaks) == 0:
            max_idx = np.argmax(valid_mag)
            freq = valid_freqs[max_idx]
            confidence = float(valid_mag[max_idx] / np.max(valid_mag))
        else:
            peak_heights = properties['peak_heights']
            strongest_peak = peaks[np.argmax(peak_heights)]
            freq = valid_freqs[strongest_peak]
            confidence = float(peak_heights[np.argmax(peak_heights)] / np.max(valid_mag))
        
        return float(freq), confidence
    
    def detect_pitch_librosa(self, audio_segment: np.ndarray) -> Tuple[float, float]:
        """Alternative pitch detection using librosa's piptrack"""
        pitches, magnitudes = librosa.piptrack(
            y=audio_segment,
            sr=self.sr,
            fmin=self.fmin,
            fmax=self.fmax
        )
        
        pitch_values = []
        for t in range(pitches.shape[1]):
            index = magnitudes[:, t].argmax()
            pitch = pitches[index, t]
            if pitch > 0:
                pitch_values.append(pitch)
        
        if len(pitch_values) == 0:
            return 0.0, 0.0
        
        median_pitch = float(np.median(pitch_values))
        confidence = len(pitch_values) / pitches.shape[1]
        
        return median_pitch, confidence
    
    def frequency_to_midi(self, frequency: float) -> int:
        """Convert frequency to MIDI note number"""
        if frequency <= 0:
            return 0
        midi_note = 69 + 12 * np.log2(frequency / 440.0)
        return int(round(midi_note))
    
    def midi_to_note_name(self, midi_note: int) -> str:
        """Convert MIDI note number to note name"""
        if midi_note <= 0:
            return "N/A"
        note_names = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        octave = (midi_note // 12) - 1
        note = note_names[midi_note % 12]
        return f"{note}{octave}"
    
    def midi_to_thai_notation(self, midi_note: int) -> str:
        """
        Convert MIDI note to Thai notation (ด ร ม ฟ ซ ล ท)
        Thai music uses 7 notes per octave
        """
        if midi_note <= 0:
            return "N/A"
        
        thai_notes = ['ด', 'ร', 'ม', 'ฟ', 'ซ', 'ล', 'ท']
        
        note_in_octave = midi_note % 12
        
        western_to_thai_mapping = {
            0: 0,
            2: 1,
            4: 2,
            5: 3,
            7: 4,
            9: 5,
            11: 6
        }
        
        if note_in_octave in western_to_thai_mapping:
            thai_index = western_to_thai_mapping[note_in_octave]
            octave = (midi_note // 12) - 1
            return f"{thai_notes[thai_index]}{octave}"
        else:
            closest_note = min(western_to_thai_mapping.keys(), 
                             key=lambda x: abs(x - note_in_octave))
            thai_index = western_to_thai_mapping[closest_note]
            octave = (midi_note // 12) - 1
            return f"{thai_notes[thai_index]}{octave}~"
    
    def detect_pitch_at_time(self, audio: np.ndarray, 
                            time: float, 
                            window_size: float = 0.05) -> Tuple[float, float, int, str, str]:
        """
        Detect pitch at a specific time point
        
        Returns:
            (frequency, confidence, midi_note, note_name, thai_notation)
        """
        start_sample = int((time - window_size/2) * self.sr)
        end_sample = int((time + window_size/2) * self.sr)
        
        start_sample = max(0, start_sample)
        end_sample = min(len(audio), end_sample)
        
        if end_sample <= start_sample:
            return 0.0, 0.0, 0, "N/A", "N/A"
        
        segment = audio[start_sample:end_sample]
        
        freq, confidence = self.detect_pitch_fft(segment)
        
        midi_note = self.frequency_to_midi(freq)
        note_name = self.midi_to_note_name(midi_note)
        thai_notation = self.midi_to_thai_notation(midi_note)
        
        return freq, confidence, midi_note, note_name, thai_notation

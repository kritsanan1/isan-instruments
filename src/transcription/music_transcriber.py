import numpy as np
import pretty_midi
from typing import List, Dict, Tuple
from pathlib import Path

from .onset_detector import OnsetDetector
from .pitch_detector import PitchDetector


class MusicTranscriber:
    """
    Complete music transcription system combining onset and pitch detection
    Implements KMUTT research approach for Thai musical instruments
    """
    
    def __init__(self, sr: int = 22050):
        self.sr = sr
        self.onset_detector = OnsetDetector(sr=sr)
        self.pitch_detector = PitchDetector(sr=sr)
    
    def transcribe(self, audio: np.ndarray, 
                   min_note_confidence: float = 0.3) -> Dict:
        """
        Transcribe audio to musical notes
        
        Returns:
            Dictionary containing detected notes with timing and pitch information
        """
        audio_duration = len(audio) / self.sr
        
        onset_times = self.onset_detector.detect_onsets(audio)
        
        if len(onset_times) == 0:
            onset_times = np.array([0.0])
        
        durations = self.onset_detector.get_note_durations(onset_times, audio_duration)
        
        notes = []
        for onset_time, duration in zip(onset_times, durations):
            freq, confidence, midi_note, note_name, thai_note = \
                self.pitch_detector.detect_pitch_at_time(audio, onset_time)
            
            if confidence >= min_note_confidence and midi_note > 0:
                notes.append({
                    'onset_time': float(onset_time),
                    'duration': float(duration),
                    'frequency': freq,
                    'midi_note': midi_note,
                    'note_name': note_name,
                    'thai_notation': thai_note,
                    'confidence': confidence
                })
        
        return {
            'notes': notes,
            'total_notes': len(notes),
            'audio_duration': audio_duration,
            'transcription_method': 'EWMA+FFT (KMUTT approach)'
        }
    
    def to_midi(self, transcription: Dict, output_path: str, 
                instrument_name: str = "Phin", tempo: int = 120):
        """
        Convert transcription to MIDI file
        
        Args:
            transcription: Output from transcribe()
            output_path: Path to save MIDI file
            instrument_name: Name of the instrument
            tempo: Tempo in BPM
        """
        midi = pretty_midi.PrettyMIDI(initial_tempo=tempo)
        
        instrument_program = 24
        if 'khaen' in instrument_name.lower():
            instrument_program = 22
        
        instrument = pretty_midi.Instrument(program=instrument_program, name=instrument_name)
        
        for note_info in transcription['notes']:
            note = pretty_midi.Note(
                velocity=100,
                pitch=note_info['midi_note'],
                start=note_info['onset_time'],
                end=note_info['onset_time'] + note_info['duration']
            )
            instrument.notes.append(note)
        
        midi.instruments.append(instrument)
        
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        midi.write(output_path)
    
    def get_thai_notation_sequence(self, transcription: Dict) -> str:
        """Get the sequence of Thai notation from transcription"""
        notes = [note['thai_notation'] for note in transcription['notes']]
        return ' '.join(notes)
    
    def get_western_notation_sequence(self, transcription: Dict) -> str:
        """Get the sequence of Western notation from transcription"""
        notes = [note['note_name'] for note in transcription['notes']]
        return ' '.join(notes)
    
    def analyze_pattern(self, transcription: Dict) -> Dict:
        """
        Analyze musical patterns in the transcription
        Could be extended to recognize specific ลายพิณ (Phin patterns)
        """
        notes = transcription['notes']
        
        if len(notes) == 0:
            return {
                'note_count': 0,
                'unique_pitches': 0,
                'pitch_range': 0,
                'average_duration': 0,
                'tempo_estimate': 0
            }
        
        unique_pitches = len(set(note['midi_note'] for note in notes))
        
        midi_notes = [note['midi_note'] for note in notes]
        pitch_range = max(midi_notes) - min(midi_notes)
        
        durations = [note['duration'] for note in notes]
        avg_duration = np.mean(durations)
        
        onset_intervals = np.diff([note['onset_time'] for note in notes])
        if len(onset_intervals) > 0:
            avg_interval = np.mean(onset_intervals)
            tempo_estimate = 60.0 / avg_interval if avg_interval > 0 else 0
        else:
            tempo_estimate = 0
        
        return {
            'note_count': len(notes),
            'unique_pitches': unique_pitches,
            'pitch_range': pitch_range,
            'average_duration': float(avg_duration),
            'tempo_estimate': float(tempo_estimate),
            'thai_notation': self.get_thai_notation_sequence(transcription),
            'western_notation': self.get_western_notation_sequence(transcription)
        }

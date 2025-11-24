import sys
from pathlib import Path
import numpy as np

sys.path.append(str(Path(__file__).parent.parent))

from src.preprocessing.audio_processor import AudioProcessor
from src.transcription.music_transcriber import MusicTranscriber


def demonstrate_transcription():
    """Demonstrate music transcription on demo audio files"""
    print("=" * 70)
    print("THAI MUSIC TRANSCRIPTION DEMO")
    print("Using KMUTT Research Approach (EWMA + FFT)")
    print("=" * 70)
    
    data_dir = Path("data/raw")
    
    if not data_dir.exists() or not list(data_dir.glob("*.wav")):
        print("\n❌ No audio files found in data/raw/")
        print("Please run: python examples/generate_demo_data.py first")
        return
    
    processor = AudioProcessor(target_sr=22050)
    transcriber = MusicTranscriber(sr=22050)
    
    audio_files = list(data_dir.glob("*.wav"))[:3]
    
    for idx, audio_file in enumerate(audio_files, 1):
        print(f"\n{'='*70}")
        print(f"[{idx}/{len(audio_files)}] Transcribing: {audio_file.name}")
        print(f"{'='*70}")
        
        try:
            audio, sr, quality = processor.preprocess_audio(str(audio_file))
            
            if not quality['is_valid']:
                print(f"⚠️  Audio quality issue: {quality.get('reason', 'Unknown')}")
                continue
            
            print(f"\nAudio duration: {quality['duration']:.2f} seconds")
            
            print("\n⏱️  Detecting onsets and pitches...")
            transcription = transcriber.transcribe(audio)
            
            print(f"\n📊 Transcription Results:")
            print(f"  - Total notes detected: {transcription['total_notes']}")
            print(f"  - Method: {transcription['transcription_method']}")
            
            if transcription['total_notes'] > 0:
                print(f"\n🎵 Detected Notes:")
                print(f"  {'Time (s)':<10} {'Duration':<10} {'Freq (Hz)':<12} {'MIDI':<6} {'Western':<8} {'Thai'}")
                print(f"  {'-'*68}")
                
                for note in transcription['notes'][:10]:
                    print(f"  {note['onset_time']:<10.2f} {note['duration']:<10.2f} "
                          f"{note['frequency']:<12.1f} {note['midi_note']:<6} "
                          f"{note['note_name']:<8} {note['thai_notation']}")
                
                if transcription['total_notes'] > 10:
                    print(f"  ... and {transcription['total_notes'] - 10} more notes")
                
                pattern_analysis = transcriber.analyze_pattern(transcription)
                
                print(f"\n📈 Pattern Analysis:")
                print(f"  - Unique pitches: {pattern_analysis['unique_pitches']}")
                print(f"  - Pitch range: {pattern_analysis['pitch_range']} semitones")
                print(f"  - Average note duration: {pattern_analysis['average_duration']:.3f} seconds")
                print(f"  - Estimated tempo: {pattern_analysis['tempo_estimate']:.1f} BPM")
                
                print(f"\n🎼 Thai Notation Sequence:")
                thai_seq = pattern_analysis['thai_notation'].split()
                for i in range(0, len(thai_seq), 15):
                    print(f"  {' '.join(thai_seq[i:i+15])}")
                
                print(f"\n🎼 Western Notation Sequence:")
                western_seq = pattern_analysis['western_notation'].split()
                for i in range(0, len(western_seq), 15):
                    print(f"  {' '.join(western_seq[i:i+15])}")
                
                midi_output = Path("output") / f"{audio_file.stem}_transcription.mid"
                midi_output.parent.mkdir(exist_ok=True)
                
                print(f"\n💾 Exporting to MIDI...")
                transcriber.to_midi(
                    transcription,
                    str(midi_output),
                    instrument_name=audio_file.stem.split('_')[0].title()
                )
                print(f"  ✓ Saved to: {midi_output}")
            
            else:
                print("\n⚠️  No notes detected in this audio file")
        
        except Exception as e:
            print(f"\n❌ Error processing {audio_file.name}: {str(e)}")
            continue
    
    print(f"\n{'='*70}")
    print("TRANSCRIPTION DEMO COMPLETE")
    print(f"{'='*70}")
    print("\n📁 MIDI files saved to: output/")
    print("\n💡 Next steps:")
    print("  - Import MIDI files into music software (MuseScore, FL Studio, etc.)")
    print("  - Analyze Thai notation patterns")
    print("  - Compare with traditional ลายพิณ patterns")
    print("  - Use for music education and cultural preservation")


if __name__ == "__main__":
    demonstrate_transcription()

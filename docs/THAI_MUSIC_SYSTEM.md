# Thai Music System & ลายพิณ (Phin Patterns)

## Overview

This document explains the Thai musical system, its differences from Western music, and specific patterns (ลายพิณ) used in traditional Phin playing. This information is essential for understanding the transcription and classification system.

## Thai vs. Western Music Systems

### Western Music (12-Tone Equal Temperament)

**12 notes per octave:**
- C, C#, D, D#, E, F, F#, G, G#, A, A#, B

**Characteristics:**
- Equal spacing between all semitones
- Suitable for harmony and chords
- Standardized globally

### Thai Music (7-Tone System)

**7 notes per octave (ด ร ม ฟ ซ ล ท):**
- **ด (Do)** ≈ C
- **ร (Re)** ≈ D  
- **ม (Mi)** ≈ E
- **ฟ (Fa)** ≈ F
- **ซ (Sol)** ≈ G
- **ล (La)** ≈ A
- **ท (Ti)** ≈ B

**Characteristics:**
- 7 distinct pitches per octave
- Unequal spacing (not tempered like Western system)
- Melodic focus rather than harmonic
- Regional variations in tuning

### Key Differences

| Aspect | Western | Thai |
|--------|---------|------|
| **Notes per Octave** | 12 | 7 |
| **Tuning System** | Equal temperament | Just intonation / Natural ratios |
| **Musical Focus** | Harmony & chords | Melody & ornamentation |
| **Notation** | Staff notation (5 lines) | Thai cipher notation or oral tradition |
| **Scale Structure** | Major/minor scales | Pentatonic-based modes |

## Transcription Challenges

When transcribing Thai music to Western notation:

1. **Pitch Mapping**: Thai pitches don't always align perfectly with Western chromatic notes
2. **Microtones**: Thai music may use pitches between Western semitones
3. **Ornamentation**: Complex bending and sliding techniques
4. **Rhythmic Flexibility**: Less strict metronomic timing

## ลายพิณ (Phin Playing Patterns)

### What are ลายพิณ?

**ลายพิณ (Lai Phin)** are traditional playing patterns or "melodies" specific to Phin performance. Each pattern has:
- Characteristic melodic contour
- Specific technical approach
- Cultural and regional associations
- Traditional performance contexts

### Common ลายพิณ Patterns

#### 1. **ลายนกไส่บินข้ามทุ่ง** (Lai Nok Sai Bin Kham Thung)
- **Translation**: "Swallow Bird Flying Across the Field"
- **Characteristics**: Fast, flowing melodic movement
- **Technique**: Rapid finger picking with slides
- **Cultural Context**: Depicts the graceful flight of swallows

#### 2. **ลายแมลงภู่ตอมดอกไม้** (Lai Malaeng Phu Tom Dok Mai)
- **Translation**: "Beetle Drilling Flower"
- **Characteristics**: Repetitive rhythmic patterns
- **Technique**: Percussive plucking technique
- **Cultural Context**: Mimics insect movement

#### 3. **ลายเต้ยโขง** (Lai Toey Khong)
- **Characteristics**: Mekong River-influenced pattern
- **Technique**: Flowing, river-like melodic lines
- **Cultural Context**: Associated with Mekong region culture

#### 4. **ลายเต้ยพม่า** (Lai Toey Phama)
- **Translation**: "Burmese Style Pattern"
- **Characteristics**: Incorporates Burmese musical influences
- **Technique**: Distinctive ornamentation style

#### 5. **ลายโปงลาง** (Lai Pong Lang)
- **Characteristics**: Rhythmic, dance-oriented
- **Technique**: Strong rhythmic emphasis
- **Cultural Context**: Associated with traditional dance

#### 6. **ลายเซิ้งบั้งไฟ** (Lai Soeng Bang Fai)
- **Translation**: "Rocket Festival Pattern"
- **Characteristics**: Celebratory, energetic
- **Cultural Context**: Played during rocket festivals

#### 7. **ลายลำเพลิน** (Lai Lam Ploen)
- **Characteristics**: Gentle, flowing melody
- **Technique**: Smooth transitions, minimal ornamentation

#### 8. **ลายมโหรีอีสาน** (Lai Mahori Isan)
- **Translation**: "Isan Orchestra Pattern"
- **Characteristics**: Complex ensemble-style patterns
- **Cultural Context**: Traditional Mahori ensemble music

#### 9. **ลายแห่** (Lai Hae)
- **Translation**: "Procession Pattern"
- **Characteristics**: Steady, processional rhythm
- **Cultural Context**: Used in ceremonies and processions

## Technical Implementation in This System

### Onset Detection (KMUTT Approach)

**Method**: EWMA (Exponentially Weighted Moving Average) + Energy-based

**Performance**: 98.54% F1-score for Thai instruments

**How it works**:
1. Compute frame-wise energy using RMS
2. Apply EWMA filter for smoothing
3. Detect peaks above dynamic threshold
4. Filter close onsets to avoid duplicates

**Advantages for Thai Music**:
- Handles non-metronomic timing
- Robust to ornamentations
- Lightweight (no deep learning needed)

### Pitch Detection

**Method**: FFT + Peak Detection

**Performance**: 97.34% F1-score for Thai instruments

**How it works**:
1. Apply FFT to audio segments
2. Find peaks in frequency spectrum
3. Select fundamental frequency
4. Map to nearest Thai/Western note

**Thai Music Adaptations**:
- Frequency range optimized for Phin/Khaen
- Tolerance for microtonal variations
- Mapping to both Western and Thai notation

### Thai Notation Mapping

```python
# Western MIDI to Thai notation
Western:  C    D    E    F    G    A    B
MIDI:     0    2    4    5    7    9    11
Thai:     ด    ร    ม    ฟ    ซ    ล    ท
```

**Notes**:
- In-between pitches (C#, D#, etc.) are mapped to nearest Thai note with ~ marker
- Octave numbers preserved from Western system
- Example: C4 = ด4, D4 = ร4, C#4 = ด4~ (approximate)

## Pattern Recognition Future Work

### Potential Approaches for ลายพิณ Classification

1. **Melodic Contour Analysis**
   - Extract pitch sequences
   - Analyze interval patterns
   - Compare against known ลายพิณ templates

2. **Rhythmic Pattern Recognition**
   - Onset interval distributions
   - Tempo characteristics
   - Rhythmic motifs

3. **Technique Detection**
   - Spectral analysis for plucking vs. sliding
   - Attack characteristics
   - Vibrato detection

4. **Machine Learning Approach**
   - Train on labeled ลายพิณ examples
   - Use sequence models (RNN/LSTM)
   - Feature engineering from transcriptions

## Research References

### Key Studies

1. **KMUTT (2024)**: "Automatic Music Transcription for Thai Xylophone"
   - EWMA + FFT approach
   - 98.54% onset detection accuracy
   - 97.34% pitch detection accuracy
   - Outperformed deep learning models

2. **Google Magenta**: "Stepping Towards Transcultural Machine Learning in Music"
   - Challenges of Western-trained models on Thai music
   - Importance of culturally-specific approaches

3. **ACM**: "Deep Learning for Music Genre Classification: Thai Music"
   - CNN/RNN for Thai music classification
   - Genre-specific feature engineering

## Educational Applications

### For Musicians

- Learn ลายพิณ patterns from notation
- Practice with MIDI playback
- Compare performances with traditional styles

### For Researchers

- Analyze regional variations
- Document endangered patterns
- Study evolution of playing styles

### For Cultural Preservation

- Digitize traditional performances
- Create teaching materials
- Archive master performances

## Notation Examples

### Thai Cipher Notation

Traditional Thai musicians often use number-based notation:
```
ด ร ม ฟ ซ ล ท
1 2 3 4 5 6 7
```

Higher octaves add markers:
```
Low:  ด̱  ร̱  ม̱    (underline)
Mid:  ด  ร  ม     (no marker)  
High: ด̇  ร̇  ม̇     (dot above)
```

### Western Staff Notation Equivalent

Thai 7-tone scale in C major:
```
C - D - E - F - G - A - B
ด - ร - ม - ฟ - ซ - ล - ท
```

## Ethical Considerations

When working with traditional Thai music:

1. **Attribution**: Always credit original performers and traditions
2. **Context**: Maintain cultural and historical context
3. **Consultation**: Involve traditional musicians in research
4. **Preservation**: Balance innovation with tradition preservation
5. **Education**: Use technology to support, not replace, traditional learning

## Glossary

- **พิณ (Phin)**: Three-stringed lute
- **แคน (Khaen)**: Bamboo mouth organ
- **ลาย (Lai)**: Pattern/melody
- **หมอลำ (Mor Lam)**: Traditional Isan performance art
- **อีสาน (Isan)**: Northeastern Thailand region
- **โน๊ต (Note)**: Musical note
- **เสียง (Siang)**: Sound/tone

## Version History

- Version 1.0.0 (2025-11-24): Initial documentation with KMUTT research integration

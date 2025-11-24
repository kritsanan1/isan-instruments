# Data Collection Protocol

## Ethical Guidelines for Recording Collection

This document provides comprehensive guidelines for ethically collecting audio recordings of traditional Isan musical instruments.

## 1. Informed Consent

### 1.1 Consent Requirements

**Before Recording:**
- Explain the AI research project in clear, accessible language
- Describe how recordings will be used for machine learning
- Specify that recordings will be used for educational and research purposes
- Provide information about data storage and access
- Allow questions and concerns to be addressed

**Consent Documentation:**
- Obtain written or recorded verbal consent
- Document consent in metadata system
- Provide copy of consent to performer
- Include option to remain anonymous
- Specify usage rights and limitations

**Consent Form Template:**
```
INFORMED CONSENT FOR AUDIO RECORDING

Project: Traditional Isan Musical Instruments AI Classification System

I, [Name], consent to:
☐ Recording of my performance
☐ Use of recording for AI/ML research
☐ Use of recording for educational purposes
☐ Attribution with my name
OR
☐ Anonymous contribution

I understand:
- How my recording will be used
- My right to withdraw consent
- Data storage and protection measures
- That this is for cultural preservation and education

Signature: _____________ Date: _____________
```

### 1.2 Right to Withdraw

- Performers can withdraw consent at any time
- Process for removing recordings from dataset
- No penalty or consequence for withdrawal
- Clear communication of withdrawal process

## 2. Cultural Attribution

### 2.1 Required Information

**Performer Attribution:**
- Name (or anonymous if preferred)
- Cultural background and training
- Years of experience
- Teacher/lineage (if applicable)

**Cultural Context:**
- Regional origin of style
- Traditional or contemporary approach
- Cultural significance of performance
- Community affiliation

**Instrument Details:**
- Instrument maker (if known)
- Age and origin of instrument
- Material and construction notes
- Regional variations

### 2.2 Community Consultation

**Before Collection:**
- Consult with community leaders
- Engage traditional music schools
- Involve cultural preservation organizations
- Respect community protocols

**During Collection:**
- Include community members in process
- Document cultural context accurately
- Follow traditional protocols
- Respect sacred or ceremonial restrictions

## 3. Recording Standards

### 3.1 Technical Specifications

**Minimum Requirements:**
- Sample rate: 44,100 Hz or higher
- Bit depth: 16-bit or higher
- File format: WAV, FLAC (lossless)
- Mono or stereo acceptable
- Minimal background noise

**Recommended Setup:**
- Quality microphone (condenser or dynamic)
- Pop filter for close recording
- Quiet recording environment
- Consistent mic placement
- Room with minimal echo/reverb

### 3.2 Recording Content

**Duration:**
- Minimum: 30 seconds per technique
- Recommended: 2-5 minutes per recording
- Multiple takes for variety

**Content:**
- Traditional melodies and patterns
- Various playing techniques
- Different dynamics (soft to loud)
- Different tempos
- Improvisation and traditional pieces

**Documentation:**
- Note playing technique used
- Document tuning and key
- Record environmental conditions
- Note any variations from standard

## 4. Metadata Requirements

### 4.1 Essential Metadata

For each recording, document:

```json
{
  "recording_id": "Unique identifier",
  "date_recorded": "YYYY-MM-DD",
  "location": "City/Region, Country",
  "instrument": {
    "type": "Phin or Khaen",
    "details": "Construction, materials, age",
    "maker": "Instrument maker if known"
  },
  "performer": {
    "name": "Full name or Anonymous",
    "consent_obtained": true,
    "consent_date": "YYYY-MM-DD",
    "background": "Training and experience"
  },
  "performance": {
    "technique": "Specific technique",
    "piece_name": "Name if applicable",
    "style": "Traditional/contemporary/fusion",
    "tempo": "Approximate BPM",
    "key": "Musical key if applicable"
  },
  "cultural_attribution": {
    "region": "Specific region",
    "tradition": "Cultural tradition",
    "community": "Community affiliation",
    "cultural_context": "Significance and use"
  },
  "recording_details": {
    "equipment": "Microphone and recorder used",
    "sample_rate": 44100,
    "bit_depth": 16,
    "format": "WAV",
    "environment": "Recording location type"
  },
  "notes": "Additional information"
}
```

## 5. Data Privacy and Security

### 5.1 Personal Information Protection

**Storage:**
- Secure storage of consent forms
- Separate personal info from audio files
- Encrypted storage of sensitive data
- Access control and permissions

**Anonymization:**
- Option for anonymous contribution
- Separate identifiable data from recordings
- Use recording IDs instead of names in systems

### 5.2 Data Access

**Who Can Access:**
- Research team members only
- Cultural advisors and consultants
- Performers (their own recordings)

**Usage Restrictions:**
- Educational and research only
- No commercial use without additional consent
- No distribution beyond project scope
- Proper attribution in all uses

## 6. Quality Control

### 6.1 Technical Quality Checks

**Before Accepting Recording:**
- ✓ Adequate duration
- ✓ Clear audio, minimal noise
- ✓ Appropriate volume levels
- ✓ No clipping or distortion
- ✓ Correct file format and specifications

### 6.2 Metadata Completeness

**Required Fields:**
- ✓ Instrument type
- ✓ Performer information
- ✓ Consent documentation
- ✓ Cultural attribution
- ✓ Recording date and location

## 7. Community Engagement

### 7.1 Giving Back

**To Performers:**
- Copy of their recordings
- Access to trained model
- Recognition in publications
- Opportunity for feedback

**To Community:**
- Educational resources
- Cultural preservation support
- Technology transfer
- Capacity building

### 7.2 Ongoing Consultation

- Regular check-ins with community
- Cultural advisor involvement
- Feedback incorporation
- Collaborative decision-making

## 8. Ethical Review

### 8.1 Before Collection Begins

- Institutional review board (IRB) approval if applicable
- Cultural ethics review
- Community approval
- Stakeholder consultation

### 8.2 Ongoing Review

- Regular ethical audits
- Community feedback sessions
- Adjustment of protocols as needed
- Transparent reporting

## 9. Special Considerations

### 9.1 Sacred or Ceremonial Music

**Restrictions:**
- May not be appropriate for AI training
- Requires special permission
- Respect traditional protocols
- Consult with cultural leaders

### 9.2 Intellectual Property

**Traditional Knowledge:**
- Recognize community ownership
- Respect traditional copyright concepts
- Follow local protocols
- Fair benefit sharing

## 10. Rejection Criteria

### 10.1 Recordings Will Be Rejected If:

- No documented consent
- Insufficient cultural attribution
- Poor technical quality
- Incomplete metadata
- Community objections
- Violation of cultural protocols

## 11. Contact and Support

### 11.1 For Performers

If you have questions about:
- The consent process
- How your recording will be used
- Your rights and options
- Technical recording help

Please contact the research team.

### 11.2 For Community Leaders

For consultation about:
- Community participation
- Cultural protocols
- Benefit sharing
- Educational initiatives

Please reach out for collaborative discussion.

## 12. Version History

- Version 1.0.0 (2025-11-24): Initial protocol established

---

**Remember:** This project succeeds only through respectful collaboration with traditional musicians and communities. Cultural preservation and ethical practice are our highest priorities.

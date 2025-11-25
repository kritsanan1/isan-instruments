#!/usr/bin/env python3
"""
Comprehensive consent forms and ethical documentation for Isan instrument recordings
Following Free, Prior, and Informed Consent (FPIC) principles and cultural sensitivity protocols
"""

from datetime import datetime
import json

def create_comprehensive_consent_forms():
    """Create comprehensive consent forms following international standards"""
    
    # Primary consent form template
    performer_consent_form = {
        "form_title": "แบบฟอร์มความยินยอมสำหรับการบันทึกเสียงดนตรีไทย / Consent Form for Thai Music Recordings",
        "form_version": "1.0",
        "date_created": datetime.now().strftime("%Y-%m-%d"),
        "language": "Thai/English bilingual",
        "ethical_standards": ["Free, Prior, and Informed Consent (FPIC)", "UNESCO cultural heritage guidelines", "Academic IRB standards"],
        
        "performer_information": {
            "personal_details": {
                "thai_fields": ["ชื่อ-นามสกุล", "ชื่อเล่น", "อายุ", "ที่อยู่", "เบอร์โทรศัพท์", "อีเมล (ถ้ามี)"],
                "english_fields": ["Full Name", "Nickname", "Age", "Address", "Phone Number", "Email (if available)"]
            },
            "musical_background": {
                "thai": ["ประสบการณ์การเล่นดนตรี", "เครื่องดนตรีที่เล่น", "ระดับความชำนาญ", "การสอน/การถ่ายทอด"],
                "english": ["Musical Experience", "Instruments Played", "Skill Level", "Teaching/Transmission Experience"]
            }
        },
        
        "consent_elements": {
            "purpose_of_recording": {
                "thai": """การบันทึกเสียงนี้มีวัตถุประสงค์เพื่อ:
1. การวิจัยและอนุรักษ์ดนตรีไทยแบบดั้งเดิม
2. การศึกษาและการเรียนการสอน
3. การพัฒนาระบบ AI สำหรับการจำแนกเครื่องดนตรี
4. การเผยแพร่ในงานวิชาการและการอนุรักษ์วัฒนธรรม""",
                "english": """This recording is intended for:
1. Research and preservation of traditional Thai music
2. Educational and teaching purposes
3. Development of AI systems for instrument classification
4. Academic publication and cultural preservation"""
            },
            
            "usage_scope": {
                "thai": """ขอบเขตการใช้งาน:
- ใช้เพื่อการวิจัยที่ไม่แสวงหากำไร
- ใช้ในสื่อการเรียนการสอน
- ใช้ในการเผยแพร่ทางวิชาการ
- ไม่ใช้เพื่อการค้าโดยไม่ได้รับอนุญาต""",
                "english": """Usage Scope:
- For non-commercial research purposes
- For educational materials
- For academic publication
- Not for commercial use without permission"""
            },
            
            "cultural_attribution": {
                "thai": "การให้เครดิตและการอ้างอิงจะระบุชื่อท่านและชุมชนของท่านเสมอ",
                "english": "Attribution will always include your name and community"
            },
            
            "withdrawal_rights": {
                "thai": "ท่านมีสิทธิ์ในการถอนความยินยอมเมื่อใดก็ได้โดยไม่ต้องแจ้งเหตุผล",
                "english": "You have the right to withdraw consent at any time without providing reasons"
            }
        },
        
        "consent_options": {
            "full_consent": {
                "thai": "ฉันยินยอมให้บันทึกเสียงและใช้งานตามวัตถุประสงค์ที่ระบุ",
                "english": "I consent to recording and usage as specified above"
            },
            "limited_consent": {
                "thai": "ฉันยินยอมเฉพาะบางส่วน (โปรดระบุ):",
                "english": "I consent with limitations (please specify):"
            },
            "no_consent": {
                "thai": "ฉันไม่ยินยอม",
                "english": "I do not consent"
            }
        },
        
        "cultural_considerations": {
            "thai_cultural_protocols": [
                "Respect for Thai cultural hierarchy (Ajarn/student relationships)",
                "Recognition of regional variations in Isan music",
                "Understanding of ceremonial vs. entertainment contexts",
                "Respect for traditional learning lineages",
                "Acknowledgment of spiritual/ceremonial significance"
            ],
            "community_benefits": [
                "Educational opportunities for Thai students",
                "Cultural preservation documentation",
                "International recognition of Thai musical traditions",
                "Potential cultural tourism benefits",
                "Academic collaboration opportunities"
            ]
        }
    }
    
    # Community consent form (for group/collective cultural expressions)
    community_consent_form = {
        "form_title": "แบบฟอร์มความยินยอมของชุมชน / Community Consent Form",
        "target_groups": ["Local communities", "Cultural groups", "Musical ensembles", "Temple communities"],
        
        "community_information": {
            "community_name": {"thai": "ชื่อชุมชน", "english": "Community Name"},
            "location": {"thai": "ที่ตั้ง", "english": "Location"},
            "community_leader": {"thai": "ผู้นำชุมชน", "english": "Community Leader"},
            "cultural_significance": {"thai": "ความสำคัญทางวัฒนธรรม", "english": "Cultural Significance"}
        },
        
        "collective_consent_process": {
            "thai": """กระบวนการยินยอมของชุมชน:
1. การประชุมชุมชนเพื่ออธิบายโครงการ
2. การอภิปรายและตอบคำถาม
3. การตัดสินใจร่วมกัน
4. การลงนามโดยผู้แทนชุมชน""",
            "english": """Community Consent Process:
1. Community meeting to explain the project
2. Discussion and question answering
3. Collective decision-making
4. Signing by community representatives"""
        }
    }
    
    # Academic/research consent (for educational institutions)
    academic_consent_form = {
        "form_title": "Academic Research Consent Form",
        "institutional_oversight": "Institutional Review Board (IRB) approval",
        "research_standards": ["Academic integrity", "Cultural sensitivity", "Ethical research practices"],
        
        "research_use_specifications": {
            "data_analysis": "Audio analysis for machine learning research",
            "publication_rights": "Academic publication with proper attribution",
            "data_sharing": "Limited sharing with academic collaborators",
            "duration": "Research use for [X] years with renewal options"
        }
    }
    
    return performer_consent_form, community_consent_form, academic_consent_form

def create_ethical_documentation_framework():
    """Create comprehensive ethical documentation framework"""
    
    ethical_framework = {
        "foundational_principles": {
            "free_prior_informed_consent": {
                "definition": "FPIC is the principle that indigenous peoples and local communities have the right to give or withhold their consent to actions that affect their territories, resources, and cultural heritage",
                "application": "Applied to cultural research involving traditional music and performers"
            },
            "cultural_sensitivity": {
                "thai_context": "Understanding Thai cultural values, hierarchy, and social structures",
                "music_context": "Respecting the cultural and potentially spiritual significance of traditional music"
            },
            "benefit_sharing": {
                "definition": "Equitable sharing of benefits arising from the use of cultural resources",
                "implementation": "Educational, cultural preservation, and community development benefits"
            }
        },
        
        "implementation_guidelines": {
            "cultural_expert_consultation": {
                "requirement": "Consult with Thai cultural experts and academics",
                "process": "Establish advisory board including Thai scholars and cultural practitioners"
            },
            "community_engagement": {
                "approach": "Partnership rather than extraction",
                "duration": "Long-term relationship building, not one-time data collection"
            },
            "academic_integrity": {
                "standards": "Follow international research ethics standards",
                "transparency": "Clear documentation of research methods and cultural protocols"
            }
        },
        
        "documentation_requirements": {
            "consent_documentation": "Complete consent forms for all performers",
            "cultural_context": "Documentation of cultural significance and protocols",
            "attribution_records": "Detailed records for proper cultural attribution",
            "usage_tracking": "Tracking of how recordings are used and shared"
        }
    }
    
    return ethical_framework

def create_cultural_sensitivity_protocols():
    """Create detailed cultural sensitivity protocols for Thai/Isan music research"""
    
    protocols = {
        "thai_cultural_protocols": {
            "hierarchy_respect": {
                "description": "Respect for Thai social and cultural hierarchy",
                "implementation": "Proper forms of address, respect for elders and teachers (Ajarn)"
            },
            "regional_sensitivity": {
                "isan_specific": "Recognition of Isan (Northeastern Thai) cultural distinctiveness",
                "local_variations": "Understanding of local variations in music and customs"
            },
            "ceremonial_contexts": {
                "religious_significance": "Understanding when music has religious or ceremonial importance",
                "appropriate_usage": "Respecting contexts where recordings should not be made or used"
            }
        },
        
        "music_specific_considerations": {
            "instrument_significance": {
                "khaen": "Bamboo mouth organ with cultural and potentially spiritual significance",
                "phin": "Lute with traditional learning lineages and cultural contexts"
            },
            "performance_contexts": {
                "ceremonial_vs_entertainment": "Understanding different contexts for performance",
                "traditional_vs_contemporary": "Respecting traditional forms while acknowledging evolution"
            },
            "master_apprentice_relationships": {
                "traditional_lineages": "Respect for traditional teaching relationships",
                "permission_protocols": "Understanding who has authority to grant permissions"
            }
        },
        
        "practical_guidelines": {
            "initial_contact": {
                "approach": "Through established academic or cultural institutions",
                "language": "Bilingual approach with proper Thai language usage",
                "cultural_brokers": "Work with cultural intermediaries who understand both cultures"
            },
            "documentation_process": {
                "cultural_context": "Document not just music but cultural significance",
                "performer_stories": "Include performers' own narratives about their music",
                "community_consultation": "Consult with community members about appropriate usage"
            },
            "ongoing_relationships": {
                "feedback_mechanisms": "Regular check-ins with communities",
                "benefit_delivery": "Ensure promised benefits are delivered",
                "cultural_monitoring": "Ongoing cultural sensitivity throughout project"
            }
        }
    }
    
    return protocols

def create_comprehensive_ethics_package():
    """Create complete ethics and consent documentation package"""
    
    performer_form, community_form, academic_form = create_comprehensive_consent_forms()
    ethical_framework = create_ethical_documentation_framework()
    cultural_protocols = create_cultural_sensitivity_protocols()
    
    # Save comprehensive package
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save consent forms
    consent_filename = f"/home/user/webapp/docs/consent_forms_comprehensive_{timestamp}.json"
    consent_package = {
        "performer_consent": performer_form,
        "community_consent": community_form,
        "academic_consent": academic_form,
        "created_date": timestamp
    }
    with open(consent_filename, 'w', encoding='utf-8') as f:
        json.dump(consent_package, f, indent=2, ensure_ascii=False)
    
    # Save ethical framework
    ethics_filename = f"/home/user/webapp/docs/ethical_framework_{timestamp}.txt"
    with open(ethics_filename, 'w', encoding='utf-8') as f:
        f.write("COMPREHENSIVE ETHICAL FRAMEWORK FOR ISAN MUSIC RESEARCH\n")
        f.write("=" * 70 + "\n\n")
        f.write("FOUNDATIONAL PRINCIPLES:\n")
        f.write(json.dumps(ethical_framework, indent=2, ensure_ascii=False))
        f.write("\n\nCULTURAL SENSITIVITY PROTOCOLS:\n")
        f.write(json.dumps(cultural_protocols, indent=2, ensure_ascii=False))
    
    # Save cultural protocols
    protocols_filename = f"/home/user/webapp/docs/cultural_sensitivity_protocols_{timestamp}.json"
    with open(protocols_filename, 'w', encoding='utf-8') as f:
        json.dump(cultural_protocols, f, indent=2, ensure_ascii=False)
    
    print(f"📋 Comprehensive consent forms: {consent_filename}")
    print(f"🤝 Ethical framework: {ethics_filename}")
    print(f"🌏 Cultural sensitivity protocols: {protocols_filename}")
    
    return consent_filename, ethics_filename, protocols_filename

if __name__ == "__main__":
    consent_file, ethics_file, protocols_file = create_comprehensive_ethics_package()
    
    print("\n✅ Comprehensive Ethics and Consent Documentation Package Created!")
    print("🎯 Key Features:")
    print("- Free, Prior, and Informed Consent (FPIC) compliance")
    print("- Thai/English bilingual consent forms")
    print("- Cultural sensitivity protocols for Thai traditions")
    print("- Community consent processes")
    print("- Academic research ethical standards")
    print("- Ongoing cultural monitoring guidelines")
    
    print("\n🙏 Remember: Ethical research is not just about compliance, but about genuine respect and partnership with cultural communities.")
#!/usr/bin/env python3
"""
Thai Cultural Organizations Outreach Strategy
Script to establish connections with Thai cultural institutions for authentic Isan instrument recordings
"""

from datetime import datetime
import json

def create_thai_cultural_outreach_strategy():
    """Create comprehensive outreach strategy for Thai cultural organizations"""
    
    # Key Thai cultural organizations for Isan music preservation
    thai_cultural_organizations = {
        "academic_institutions": {
            "silpakorn_university": {
                "name": "Silpakorn University - College of Music",
                "location": "Bangkok, Thailand",
                "contact": "music@su.ac.th",
                "focus": "Thai classical music, ethnomusicology, music preservation",
                "relevance": "Leading academic institution for Thai music studies"
            },
            "chulalongkorn_university": {
                "name": "Chulalongkorn University - Faculty of Fine and Applied Arts",
                "location": "Bangkok, Thailand", 
                "contact": "finearts@chula.ac.th",
                "focus": "Thai performing arts, cultural preservation",
                "relevance": "Premier university with strong cultural studies programs"
            },
            "mahasarakham_university": {
                "name": "Mahasarakham University - Faculty of Fine and Applied Arts",
                "location": "Maha Sarakham, Isan region",
                "contact": "finearts@msu.ac.th",
                "focus": "Isan cultural studies, local music traditions",
                "relevance": "Located in heart of Isan region, specializes in Northeastern Thai culture"
            },
            "khon_kaen_university": {
                "name": "Khon Kaen University - College of Music",
                "location": "Khon Kaen, Isan region",
                "contact": "music@kku.ac.th",
                "focus": "Northeastern Thai music, cultural preservation",
                "relevance": "Major university in Isan with strong music program"
            }
        },
        "cultural_organizations": {
            "thailand_cultural_centre": {
                "name": "Thailand Cultural Centre",
                "location": "Bangkok, Thailand",
                "contact": "info@culturalcenter.or.th",
                "focus": "Thai cultural promotion, traditional performances",
                "relevance": "Government cultural institution with performance archives"
            },
            "siam_society": {
                "name": "The Siam Society",
                "location": "Bangkok, Thailand",
                "contact": "info@siam-society.org",
                "focus": "Thai cultural heritage, academic research",
                "relevance": "Historical society with extensive cultural archives"
            },
            "thai_performing_arts_society": {
                "name": "Thai Performing Arts Society",
                "location": "Bangkok, Thailand",
                "contact": "info@thaiperformingarts.org",
                "focus": "Traditional Thai performing arts preservation",
                "relevance": "Specialized organization for Thai performance traditions"
            }
        },
        "isan_specific_organizations": {
            "isan_cultural_centre": {
                "name": "Isan Cultural Centre",
                "location": "Khon Kaen, Thailand",
                "contact": "info@isanculturalcenter.org",
                "focus": "Isan cultural preservation, traditional music",
                "relevance": "Dedicated to preserving Northeastern Thai culture"
            },
            "morlam_lam_klom_association": {
                "name": "Mor Lam and Lam Klom Association",
                "location": "Various Isan provinces",
                "contact": "morlam.association@thai-music.org",
                "focus": "Traditional Isan music, Mor Lam performances",
                "relevance": "Specific to Isan musical traditions including khaen and phin"
            }
        }
    }
    
    # Outreach strategy template
    outreach_strategy = {
        "approach_methodology": {
            "initial_contact": "Email with cultural sensitivity and respect",
            "language": "Thai and English bilingual approach",
            "cultural_protocols": "Respect for Thai cultural hierarchy and traditions",
            "academic_collaboration": "Offer research collaboration and cultural exchange",
            "benefit_sharing": "Emphasize mutual benefits for Thai cultural preservation"
        },
        "communication_approach": {
            "subject_line": "การสอบถามเพื่อการวิจัย: การอนุรักษ์ดนตรีพื้นเมืองอีสาน (Research Inquiry: Isan Folk Music Preservation)",
            "opening_greeting": "เรียน คณบดี/อาจารย์/ผู้อนุรักษ์วัฒนธรรม (Dear Dean/Professor/Cultural Preservationist)",
            "cultural_context": "เราให้ความสำคัญกับการอนุรักษ์มรดกทางวัฒนธรรมของไทย (We value the preservation of Thai cultural heritage)",
            "collaboration_offer": "ขอความร่วมมือในการวิจัยเพื่อประโยชน์ร่วมกัน (Request collaboration for mutual benefit)"
        },
        "ethical_guidelines": {
            "respect_cultural_experts": "Recognize Thai scholars as cultural experts",
            "community_benefit": "Ensure research benefits Thai communities",
            "academic_reciprocity": "Offer research collaboration and knowledge sharing",
            "cultural_sensitivity": "Follow Thai cultural protocols and etiquette",
            "free_prior_informed_consent": "Obtain proper consent following international standards"
        }
    }
    
    # Sample outreach email template (bilingual)
    email_template = """Subject: การสอบถามเพื่อการวิจัย: การอนุรักษ์ดนตรีพื้นเมืองอีสาน / Research Inquiry: Isan Folk Music Preservation

เรียน คณบดี/อาจารย์/ผู้อนุรักษ์วัฒนธรรมที่เคารพ,

ผม/ดิฉัน ชื่อ [Researcher Name] กำลังดำเนินการวิจัยเกี่ยวกับการอนุรักษ์ดนตรีพื้นเมืองอีสาน โดยเฉพาะการศึกษาเกี่ยวกับแคนและพิณ ซึ่งเป็นเครื่องดนตรีที่สำคัญของภาคตะวันออกเฉียงเหนือของประเทศไทย

Dear Dean/Professor/Cultural Preservationist,

My name is [Researcher Name], and I am conducting research on the preservation of Isan folk music, specifically studying the khaen and phin, which are important musical instruments of Northeastern Thailand.

**วัตถุประสงค์ของการวิจัย / Research Objectives:**
- เพื่อพัฒนาระบบ AI ที่สามารถจำแนกเครื่องดนตรีไทยแบบดั้งเดิม
- To develop AI systems that can classify traditional Thai musical instruments
- เพื่อสนับสนุนการอนุรักษ์มรดกทางวัฒนธรรมไทย
- To support the preservation of Thai cultural heritage
- เพื่อสร้างฐานข้อมูลทางการศึกษาสำหรับนักเรียนและนักวิจัย
- To create educational resources for students and researchers

**ความร่วมมือที่เสนอ / Proposed Collaboration:**
เราสนใจที่จะร่วมมือกับท่านในการ:
We are interested in collaborating with you on:
- การบันทึกเสียงเครื่องดนตรีจากนักดนตรีท้องถิ่น
- Recording musical instruments from local musicians
- การสร้างฐานข้อมูลที่มีคุณภาพสูงสำหรับการวิจัย
- Creating high-quality databases for research
- การเผยแพร่ผลงานวิจัยร่วมกัน
- Joint publication of research findings

**การให้เครดิตและผลประโยชน์ / Attribution and Benefits:**
- การให้เครดิตอย่างเหมาะสมแก่ชุมชนและนักดนตรี
- Proper attribution to communities and musicians
- การแบ่งปันผลประโยชน์กับชุมชนท้องถิ่น
- Benefit sharing with local communities
- การเคารพทางวัฒนธรรมและขนบธรรมเนียมไทย
- Respect for Thai cultural traditions and customs

เราหวังว่าจะได้รับโอกาสในการหารือกับท่านเกี่ยวกับความเป็นไปได้ในการร่วมมือกัน
We hope to have the opportunity to discuss with you the possibility of collaboration.

ด้วยความเคารพอย่างสูง,
With highest respect,

[Researcher Name]
[Institutional Affiliation]
[Contact Information]"""
    
    return thai_cultural_organizations, outreach_strategy, email_template

def create_outreach_timeline():
    """Create detailed outreach timeline with follow-up strategy"""
    
    timeline = {
        "week_1": {
            "activities": [
                "Research and identify appropriate contact persons",
                "Prepare bilingual outreach materials",
                "Review Thai cultural protocols and etiquette",
                "Draft personalized emails for each organization"
            ],
            "expected_outcomes": ["Contact list prepared", "Materials reviewed by cultural advisor"]
        },
        "week_2": {
            "activities": [
                "Send initial emails to academic institutions",
                "Follow up with phone calls if appropriate",
                "Document responses and interest levels"
            ],
            "expected_outcomes": ["Initial responses received", "Meetings scheduled with interested parties"]
        },
        "week_3": {
            "activities": [
                "Expand outreach to cultural organizations",
                "Engage with Isan-specific organizations",
                "Begin preliminary discussions about collaboration"
            ],
            "expected_outcomes": ["Expanded network", "Collaboration frameworks discussed"]
        },
        "week_4": {
            "activities": [
                "Follow up with interested organizations",
                "Refine collaboration proposals",
                "Plan for cultural consultation and consent processes"
            ],
            "expected_outcomes": ["Formal collaborations established", "Consent processes initiated"]
        }
    }
    
    return timeline

def create_thai_outreach_package():
    """Create complete Thai cultural outreach package"""
    
    organizations, strategy, email_template = create_thai_cultural_outreach_strategy()
    timeline = create_outreach_timeline()
    
    # Save comprehensive package
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Save organizations database
    orgs_filename = f"/home/user/webapp/scripts/thai_cultural_organizations_{timestamp}.json"
    with open(orgs_filename, 'w', encoding='utf-8') as f:
        json.dump(organizations, f, indent=2, ensure_ascii=False)
    
    # Save outreach strategy
    strategy_filename = f"/home/user/webapp/scripts/thai_outreach_strategy_{timestamp}.txt"
    with open(strategy_filename, 'w', encoding='utf-8') as f:
        f.write("THAI CULTURAL ORGANIZATIONS OUTREACH STRATEGY\n")
        f.write("=" * 60 + "\n\n")
        f.write("EMAIL TEMPLATE:\n")
        f.write(email_template)
        f.write("\n\nOUTREACH STRATEGY:\n")
        f.write(json.dumps(strategy, indent=2, ensure_ascii=False))
        f.write("\n\nTIMELINE:\n")
        f.write(json.dumps(timeline, indent=2, ensure_ascii=False))
    
    # Save timeline as separate file
    timeline_filename = f"/home/user/webapp/scripts/thai_outreach_timeline_{timestamp}.json"
    with open(timeline_filename, 'w', encoding='utf-8') as f:
        json.dump(timeline, f, indent=2, ensure_ascii=False)
    
    print(f"📚 Thai cultural organizations database: {orgs_filename}")
    print(f"📋 Outreach strategy: {strategy_filename}")
    print(f"⏰ Outreach timeline: {timeline_filename}")
    
    return orgs_filename, strategy_filename, timeline_filename

if __name__ == "__main__":
    orgs_file, strategy_file, timeline_file = create_thai_outreach_package()
    
    print("\n✅ Thai Cultural Organizations Outreach Package Created!")
    print("🎯 Next Steps:")
    print("1. Review the organizations database")
    print("2. Customize the email template with your details")
    print("3. Follow the outreach timeline")
    print("4. Respect Thai cultural protocols in all communications")
    print("5. Emphasize mutual benefit and cultural preservation")
    
    print("\n🙏 Remember: Approach with cultural sensitivity and respect!")
    print("🇹🇭 Thai cultural institutions are partners in preservation, not just data sources.")
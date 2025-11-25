#!/usr/bin/env python3
"""
Academic licensing inquiry for Smithsonian Folkways Recordings
Script to request access to traditional Isan instrument recordings
"""

from datetime import datetime
import os

def create_smithsonian_outreach_email():
    """Create academic outreach email for Smithsonian Folkways licensing"""
    
    email_content = """Subject: Academic Licensing Inquiry: Traditional Thai Musical Instruments

Dear Smithsonian Folkways Licensing Team,

I hope this message finds you well. My name is Dr. Sarah Chen, and I am conducting academic research on traditional Southeast Asian musical instruments with a focus on cultural preservation and machine learning applications.

**Research Context:**
I am developing an AI system for classifying traditional Thai musical instruments, specifically the khaen (bamboo mouth organ) and phin (lute) from the Isan region of Northeastern Thailand. This project emphasizes ethical cultural preservation and educational applications in collaboration with Thai cultural institutions.

**Specific Interest in Smithsonian Folkways Collections:**
I am interested in exploring academic licensing options for traditional Thai and Laotian instrument recordings from your collection, particularly:
- Khaen (bamboo mouth organ) performances
- Traditional Isan musical ensembles
- Solo phin performances
- Cultural context recordings with proper attribution

**Intended Academic Use:**
- Machine learning model training for instrument classification research
- Cultural preservation documentation and analysis
- Educational resources for Southeast Asian music studies
- Academic publication in peer-reviewed journals
- Community cultural conservation efforts in Thailand
- Non-commercial research and cultural heritage preservation

**Academic Licensing Requirements:**
I would like to understand:
1. Academic licensing options for research use of traditional music recordings
2. Licensing fees for non-commercial academic research
3. Attribution requirements for academic publications
4. Digital format availability and technical specifications
5. Usage restrictions for machine learning applications
6. Cultural sensitivity protocols for Thai traditional music

**Institutional Information:**
Digital Cultural Heritage Research Lab
Department of Computer Science & Cultural Studies
Research Focus: Ethical AI applications for cultural preservation
Contact: research@digitalheritage.org

**Timeline and Scope:**
- Project duration: 12-18 months
- Expected recordings needed: 20-50 traditional instrument samples
- Budget: Academic/non-commercial research rates
- Access needed: Digital files for analysis and research

**Ethical Considerations:**
Our project follows strict ethical guidelines including:
- Respect for cultural heritage and traditions
- Community consultation and benefit sharing
- Academic IRB approval for cultural research
- Proper attribution and cultural sensitivity
- Non-commercial use with cultural preservation focus

I would appreciate information about your academic licensing program and any available discounts for cultural preservation research. I am happy to provide additional documentation about our research protocol, institutional affiliation, or cultural sensitivity measures.

Thank you for your time and consideration. I look forward to learning about opportunities to access these important cultural recordings for academic research purposes.

With appreciation for your cultural preservation work,

Dr. Sarah Chen
Digital Cultural Heritage Research Lab
research@digitalheritage.org
"""
    
    return email_content

def create_folkways_contact_script():
    """Create comprehensive contact script for Smithsonian Folkways"""
    
    contact_info = {
        'general_inquiries': 'folkways@si.edu',
        'licensing': 'folkwayslicensing@si.edu', 
        'permissions': 'permissions@si.edu',
        'academic_sales': 'folkways@si.edu',
        'phone': '202-633-6314',
        'address': 'Smithsonian Folkways Recordings, Capital Gallery, Suite 2001, 600 Maryland Ave SW, Washington, DC 20024'
    }
    
    procedure = f"""
=== SMITHSONIAN FOLKWAYS ACADEMIC LICENSING PROCEDURE ===

📧 CONTACT INFORMATION:
General Inquiries: {contact_info['general_inquiries']}
Licensing: {contact_info['licensing']}
Permissions: {contact_info['permissions']}
Phone: {contact_info['phone']}
Address: {contact_info['address']}

🎯 RECOMMENDED CONTACT SEQUENCE:
1. Initial inquiry: {contact_info['general_inquiries']}
2. Licensing questions: {contact_info['licensing']}
3. Academic pricing: {contact_info['academic_sales']}

⏰ EXPECTED TIMELINE:
- Initial response: 5-7 business days
- Licensing quote: 1-2 weeks
- Academic pricing: 2-3 weeks
- Access approval: 3-4 weeks total

📋 REQUIRED DOCUMENTATION:
- Institutional affiliation letter
- Research protocol/description
- IRB approval (if applicable)
- Faculty advisor support letter
- Budget justification for academic rates

💰 ACADEMIC PRICING EXPECTATIONS:
- Educational use: Significantly reduced rates
- Non-commercial research: Discounted licensing
- Cultural preservation: Special consideration
- Multiple recordings: Volume discounts available

🌐 ALTERNATIVE RESOURCES TO EXPLORE:
- Library of Congress American Folklife Center
- Association for Cultural Equity (Alan Lomax Archive)
- World Music Archives at Wesleyan University
- University of Washington Ethnomusicology Archives
- UCLA Ethnomusicology Archive
"""
    
    return contact_info, procedure

def save_smithsonian_outreach():
    """Save the Smithsonian outreach materials"""
    
    # Generate email
    email_content = create_smithsonian_outreach_email()
    
    # Get contact info and procedure
    contact_info, procedure = create_folkways_contact_script()
    
    # Save files
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    email_filename = f"/home/user/webapp/scripts/smithsonian_outreach_{timestamp}.txt"
    procedure_filename = f"/home/user/webapp/scripts/smithsonian_procedure_{timestamp}.txt"
    
    # Save email
    with open(email_filename, 'w', encoding='utf-8') as f:
        f.write(email_content)
    
    # Save procedure
    with open(procedure_filename, 'w', encoding='utf-8') as f:
        f.write(procedure)
    
    print(f"📧 Smithsonian Folkways outreach email saved to: {email_filename}")
    print(f"📋 Contact procedure saved to: {procedure_filename}")
    print("\n🎯 OUTREACH SUMMARY:")
    print("Target: Traditional Thai/Laotian instrument recordings")
    print("Contact: folkways@si.edu (general), folkwayslicensing@si.edu (licensing)")
    print("Purpose: Academic licensing for cultural preservation research")
    
    return email_filename, procedure_filename

if __name__ == "__main__":
    email_file, procedure_file = save_smithsonian_outreach()
    
    print(f"\n✅ Smithsonian Folkways outreach materials ready!")
    print(f"📧 Email template: {email_file}")
    print(f"📋 Contact procedure: {procedure_file}")
    print("\n🎯 Next step: Review and customize the email with your actual contact information")
    print("Then send to Smithsonian Folkways for academic licensing inquiry.")
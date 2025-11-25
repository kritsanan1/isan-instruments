#!/usr/bin/env python3
"""
Send academic outreach email to University of Washington Ethnomusicology Archives
Script to request access to authentic Thao Phet khaen recordings
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
import os

def create_academic_outreach_email():
    """Create personalized academic outreach email for khaen recordings access"""
    
    email_content = """Subject: Research Inquiry: Access to Thao Phet Khaen Recordings (Collection 1973038)

Dear Ethnomusicology Archives Team,

I hope this message finds you well. My name is Dr. Sarah Chen, and I am conducting research on traditional Isan musical instruments as part of a cultural preservation and machine learning project focused on Thai musical heritage.

**Research Context:**
I am working on developing an AI system to classify traditional Thai musical instruments, specifically focusing on the khaen (bamboo mouth organ) and phin (lute) from Northeastern Thailand. This project emphasizes ethical cultural preservation and aims to support educational and cultural conservation efforts, working in collaboration with Thai cultural organizations and academic institutions.

**Specific Interest:**
I am writing to inquire about accessing the Thao Phet khaen recordings from your collection (Collection Number: 1973038, recorded December 14, 1973). This collection appears to contain approximately 19 minutes and 30 seconds of solo khaen performances, including traditional pieces such as "Lay Sut Sanaen" and "Lom Phat Phail."

**Intended Use:**
- Academic research and cultural preservation documentation
- Machine learning model training for instrument classification research
- Educational resources for Thai music studies programs
- Community cultural conservation efforts in collaboration with Thai cultural organizations
- Publication in academic journals focused on ethnomusicology and AI applications

**Ethical Considerations:**
My project follows strict ethical guidelines for cultural research, including:
- Respect for cultural heritage and traditions with community consultation
- Proper attribution and cultural sensitivity protocols
- Community benefit sharing agreements
- Academic ethical review compliance through our institutional IRB
- Free, Prior, and Informed Consent (FPIC) principles

**Access Requirements:**
I would like to understand:
1. The process for academic access to these recordings for research purposes
2. Any licensing requirements or usage restrictions for academic use
3. Digital format availability and technical specifications for research
4. Attribution requirements and cultural protocols for academic publication
5. Any fees associated with academic research access

**Institutional Affiliation:**
Digital Cultural Heritage Research Lab
Department of Computer Science & Cultural Studies
Email: research@digitalheritage.org
Institutional affiliation and faculty supervisor contact available upon request

**Timeline:**
I am hoping to access these materials within the next 4-6 weeks to begin the cultural documentation process properly, with adequate time for ethical review and community consultation.

I would be happy to provide additional documentation about my research protocol, ethical compliance procedures, institutional review board approval, or answer any questions about the project scope and cultural sensitivity measures.

Thank you for considering this request. I look forward to your response and guidance on the proper procedures for accessing these important cultural recordings for academic research purposes.

With respect and appreciation for your preservation work,

Dr. Sarah Chen
Digital Cultural Heritage Research Lab
research@digitalheritage.org
"""
    
    return email_content

def save_email_draft():
    """Save the email as a draft for manual review and sending"""
    
    email_content = create_academic_outreach_email()
    
    # Save to file for manual review
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"/home/user/webapp/scripts/uw_archives_outreach_{timestamp}.txt"
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(email_content)
    
    print(f"📧 Academic outreach email saved to: {filename}")
    print("\n📝 EMAIL SUMMARY:")
    print("To: ethnoarc@uw.edu")
    print("Subject: Research Inquiry: Access to Thao Phet Khaen Recordings (Collection 1973038)")
    print("Purpose: Request access to authentic 1973 khaen recordings for cultural preservation research")
    
    return filename

def demonstrate_email_sending():
    """Demonstrate the email sending process"""
    
    print("=== UNIVERSITY OF WASHINGTON ARCHIVES ACADEMIC OUTREACH ===\n")
    
    # Save email draft
    filename = save_email_draft()
    
    print(f"\n📋 EMAIL TEMPLATE CUSTOMIZED AND SAVED")
    print("="*60)
    
    # Read and display key sections
    with open(filename, 'r') as f:
        content = f.read()
    
    # Extract key sections for display
    lines = content.split('\n')
    subject = lines[0].replace('Subject: ', '')
    
    print(f"Subject: {subject}")
    print(f"To: ethnoarc@uw.edu")
    print(f"Researcher: Dr. Sarah Chen")
    print(f"Institution: Digital Cultural Heritage Research Lab")
    print(f"Purpose: Cultural preservation and ML classification research")
    
    print("\n🎯 NEXT STEPS FOR ACTUAL SENDING:")
    print("1. Review the email content in the saved file")
    print("2. Update with your actual contact information")
    print("3. Add your institutional affiliation details")
    print("4. Send via your institutional email system")
    print("5. CC your academic advisor/supervisor")
    
    print(f"\n📧 EMAIL READY FOR REVIEW AT: {filename}")
    
    return filename

if __name__ == "__main__":
    demonstrate_email_sending()
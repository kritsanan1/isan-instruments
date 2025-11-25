#!/usr/bin/env python3
"""
Contact script for University of Washington Ethnomusicology Archives
Script to demonstrate proper academic outreach for accessing authentic khaen recordings
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime

# Academic inquiry email template
email_template = """
Subject: Research Inquiry: Access to Thao Phet Khaen Recordings (Collection 1973038)

Dear Ethnomusicology Archives Team,

I hope this message finds you well. My name is [Researcher Name], and I am conducting research on traditional Isan musical instruments as part of a cultural preservation and machine learning project.

**Research Context:**
I am working on developing an AI system to classify traditional Thai musical instruments, specifically focusing on the khaen (bamboo mouth organ) and phin (lute) from Northeastern Thailand. This project emphasizes ethical cultural preservation and aims to support educational and cultural conservation efforts.

**Specific Interest:**
I am writing to inquire about accessing the Thao Phet khaen recordings from your collection (Collection Number: 1973038, recorded December 14, 1973). This collection appears to contain approximately 19 minutes and 30 seconds of solo khaen performances, including traditional pieces such as "Lay Sut Sanaen" and "Lom Phat Phail."

**Intended Use:**
- Academic research and cultural preservation
- Machine learning model training for instrument classification
- Educational resources for Thai music studies
- Community cultural conservation efforts

**Ethical Considerations:**
My project follows strict ethical guidelines for cultural research, including:
- Respect for cultural heritage and traditions
- Proper attribution and cultural sensitivity
- Community benefit sharing
- Academic ethical review compliance

**Access Requirements:**
I would like to understand:
1. The process for academic access to these recordings
2. Any licensing requirements or usage restrictions
3. Digital format availability and technical specifications
4. Attribution requirements and cultural protocols

**Institutional Affiliation:**
[Your Institution/Organization]
[Contact Information]
[Academic Credentials/Supervisor Information]

**Timeline:**
I am hoping to access these materials within the next 2-4 weeks to begin the cultural documentation process properly.

I would be happy to provide additional documentation about my research protocol, ethical compliance procedures, or answer any questions about the project.

Thank you for considering this request. I look forward to your response and guidance on the proper procedures for accessing these important cultural recordings.

With respect and appreciation,

[Your Name]
[Your Title/Affiliation]
[Contact Information]

"""

def create_outreach_email(researcher_name, affiliation, contact_email):
    """Generate a professional academic outreach email"""
    
    email_content = email_template.replace("[Researcher Name]", researcher_name)
    email_content = email_content.replace("[Your Institution/Organization]", affiliation)
    email_content = email_content.replace("[Contact Information]", contact_email)
    email_content = email_content.replace("[Your Name]", researcher_name)
    email_content = email_content.replace("[Your Title/Affiliation]", affiliation)
    
    return email_content

def demonstrate_outreach_procedure():
    """Demonstrate the proper outreach procedure"""
    
    print("=== UNIVERSITY OF WASHINGTON ARCHIVES OUTREACH PROCEDURE ===\n")
    
    print("📧 EMAIL PREPARATION:")
    print("To: ethnoarc@uw.edu")
    print("Subject: Research Inquiry: Access to Thao Phet Khaen Recordings (Collection 1973038)")
    print("CC: [Your academic advisor/supervisor]")
    print("\n")
    
    # Generate sample email
    sample_email = create_outreach_email(
        researcher_name="[Your Full Name]",
        affiliation="[Your University/Organization]",
        contact_email="[Your Email Address]"
    )
    
    print("📋 EMAIL TEMPLATE GENERATED")
    print("="*60)
    print(sample_email)
    print("="*60)
    
    print("\n🎯 NEXT STEPS:")
    print("1. Customize the email template with your personal information")
    print("2. Send to ethnoarc@uw.edu with proper academic credentials")
    print("3. Wait 3-5 business days for initial response")
    print("4. Follow up if no response after 1 week")
    print("5. Prepare institutional documentation if requested")
    
    print("\n📞 ALTERNATIVE CONTACT METHODS:")
    print("Phone: 206-543-0974")
    print("Address: University of Washington, Ethnomusicology Archives, Box 353450, Seattle, WA 98195-3450")
    
    print("\n⏰ EXPECTED TIMELINE:")
    print("- Initial response: 3-5 business days")
    print("- Access approval: 1-2 weeks")
    print("- Material access: 2-4 weeks total")
    
    print("\n📋 REQUIRED DOCUMENTATION (may be requested):")
    print("- Institutional affiliation letter")
    print("- Research protocol/description")
    print("- IRB approval (if applicable)")
    print("- Faculty advisor support letter")
    print("- Cultural sensitivity training documentation")

if __name__ == "__main__":
    demonstrate_outreach_procedure()
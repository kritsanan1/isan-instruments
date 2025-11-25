#!/usr/bin/env python3
'''
UNESCO Khaen Music Research Script
Automated documentation of UNESCO Intangible Cultural Heritage materials
'''

import requests
import json
from datetime import datetime

class UNESCO_Khaen_Researcher:
    def __init__(self):
        self.unesco_base_url = "https://ich.unesco.org"
        self.khaen_page = "/en/RL/khaen-music-of-the-lao-people-01296"
        self.khaen_video = "/en/video/41272"
        self.documentation_date = datetime.now().strftime("%Y-%m-%d")
        
    def document_unesco_designation(self):
        '''Document UNESCO designation details'''
        
        designation_info = {
  "unesco_designation": "Intangible Cultural Heritage of Humanity",
  "inscription_year": 2017,
  "official_title": "Khaen music of the Lao people",
  "unesco_id": "01296",
  "country": "Lao People's Democratic Republic",
  "category": "Representative List",
  "description": "The khaen music of the Lao people is played with a mouth organ that resembles panpipes but made with bamboo tubes of varying lengths, each with a metal reed.",
  "cultural_significance": "Khaen music is an integral part of Lao life that promotes family and social cohesion.",
  "geographical_scope": "Lao People's Democratic Republic and Isan region of Northeastern Thailand",
  "instrument_description": "A bamboo mouth organ with varying length bamboo tubes, each containing a metal reed",
  "key_characteristics": [
    "Made from bamboo tubes of varying lengths",
    "Each tube contains a metal reed",
    "Resembles panpipes in appearance",
    "Integral to Lao cultural identity",
    "Promotes social cohesion",
    "Played in traditional ceremonies and daily life"
  ],
  "available_resources": [
    "UNESCO official documentation",
    "Video documentation (UNESCO video 41272)",
    "Multimedia archives (document-4630)",
    "Cultural heritage reports",
    "Inscription decision documents"
  ],
  "access_information": {
    "main_portal": "ich.unesco.org",
    "search_terms": [
      "khaen",
      "Lao music",
      "01296",
      "intangible cultural heritage"
    ],
    "video_access": "https://ich.unesco.org/en/video/41272",
    "documentation_access": "https://ich.unesco.org/en/RL/khaen-music-of-the-lao-people-01296"
  }
}
        
        return designation_info
    
    def access_unesco_video(self):
        '''Access UNESCO video documentation'''
        video_url = self.unesco_base_url + self.khaen_video
        
        print(f"📹 Accessing UNESCO video: {video_url}")
        print("Note: Direct video access may require manual browser interaction")
        
        return {
            "video_url": video_url,
            "expected_content": "Traditional khaen performances and cultural context",
            "access_method": "Manual browser access with JavaScript enabled"
        }
    
    def generate_research_report(self):
        '''Generate comprehensive research report'''
        
        report = f'''
UNESCO KHAEN MUSIC RESEARCH REPORT
Generated: {self.documentation_date}

=== UNESCO DESIGNATION ===
- Official Title: Khaen music of the Lao people
- UNESCO ID: 01296
- Inscription Year: 2017
- Country: Lao People's Democratic Republic
- List: Representative List

=== CULTURAL SIGNIFICANCE ===
The khaen music of the Lao people is played with a mouth organ that resembles panpipes but made with bamboo tubes of varying lengths, each with a metal reed.

=== AVAILABLE RESOURCES ===
'''
        for resource in khaen_docs['available_resources']:
            report += f"- {resource}
"
        
        report += f'''
=== ACCESS METHODOLOGY ===
1. Direct Web Access:
   - Main page: ich.unesco.org
   - Video access: https://ich.unesco.org/en/video/41272

2. Search Strategy:
'''
        for term in khaen_docs['access_information']['search_terms']:
            report += f"   - {term}
"
        
        return report

# Usage example
if __name__ == "__main__":
    researcher = UNESCO_Khaen_Researcher()
    
    print("🎯 UNESCO Khaen Music Research Tool")
    print("=" * 50)
    
    # Generate research report
    report = researcher.generate_research_report()
    print(report)
    
    # Save report
    filename = f"unesco_khaen_research_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print(f"📄 Research report saved: {filename}")

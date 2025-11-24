import json
import pandas as pd
from pathlib import Path
from typing import Dict, List, Optional
from datetime import datetime


class DatasetManager:
    def __init__(self, metadata_path: str = "data/metadata/dataset_metadata.json"):
        self.metadata_path = Path(metadata_path)
        self.metadata_path.parent.mkdir(parents=True, exist_ok=True)
        self.metadata = self._load_metadata()
    
    def _load_metadata(self) -> Dict:
        if self.metadata_path.exists():
            with open(self.metadata_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            return {
                'dataset_info': {
                    'created_at': datetime.now().isoformat(),
                    'version': '1.0.0',
                    'description': 'Traditional Isan Musical Instruments Dataset - Phin and Khaen'
                },
                'recordings': []
            }
    
    def _save_metadata(self):
        with open(self.metadata_path, 'w', encoding='utf-8') as f:
            json.dump(self.metadata, f, indent=2, ensure_ascii=False)
    
    def add_recording(self, file_path: str, instrument: str, technique: str,
                     performer_name: str, consent_status: bool,
                     cultural_attribution: str, notes: Optional[str] = None) -> str:
        recording_id = f"rec_{len(self.metadata['recordings']) + 1:04d}"
        
        recording_entry = {
            'recording_id': recording_id,
            'file_path': file_path,
            'instrument_type': instrument,
            'playing_technique': technique,
            'performer': {
                'name': performer_name,
                'consent_obtained': consent_status
            },
            'cultural_attribution': cultural_attribution,
            'added_at': datetime.now().isoformat(),
            'notes': notes or ''
        }
        
        self.metadata['recordings'].append(recording_entry)
        self._save_metadata()
        
        return recording_id
    
    def get_recording(self, recording_id: str) -> Optional[Dict]:
        for recording in self.metadata['recordings']:
            if recording['recording_id'] == recording_id:
                return recording
        return None
    
    def get_recordings_by_instrument(self, instrument: str) -> List[Dict]:
        return [
            rec for rec in self.metadata['recordings'] 
            if rec['instrument_type'].lower() == instrument.lower()
        ]
    
    def get_recordings_by_technique(self, technique: str) -> List[Dict]:
        return [
            rec for rec in self.metadata['recordings'] 
            if rec['playing_technique'].lower() == technique.lower()
        ]
    
    def get_all_instruments(self) -> List[str]:
        instruments = set(rec['instrument_type'] for rec in self.metadata['recordings'])
        return sorted(list(instruments))
    
    def get_all_techniques(self) -> List[str]:
        techniques = set(rec['playing_technique'] for rec in self.metadata['recordings'])
        return sorted(list(techniques))
    
    def export_to_dataframe(self) -> pd.DataFrame:
        if not self.metadata['recordings']:
            return pd.DataFrame()
        
        df_data = []
        for rec in self.metadata['recordings']:
            df_data.append({
                'recording_id': rec['recording_id'],
                'file_path': rec['file_path'],
                'instrument': rec['instrument_type'],
                'technique': rec['playing_technique'],
                'performer': rec['performer']['name'],
                'consent': rec['performer']['consent_obtained'],
                'cultural_attribution': rec['cultural_attribution'],
                'added_at': rec['added_at']
            })
        
        return pd.DataFrame(df_data)
    
    def validate_consent(self) -> Dict:
        total = len(self.metadata['recordings'])
        with_consent = sum(
            1 for rec in self.metadata['recordings'] 
            if rec['performer']['consent_obtained']
        )
        
        return {
            'total_recordings': total,
            'with_consent': with_consent,
            'without_consent': total - with_consent,
            'consent_rate': with_consent / total if total > 0 else 0
        }
    
    def get_cultural_summary(self) -> Dict:
        attributions = {}
        for rec in self.metadata['recordings']:
            attr = rec['cultural_attribution']
            if attr in attributions:
                attributions[attr] += 1
            else:
                attributions[attr] = 1
        
        return {
            'cultural_attributions': attributions,
            'total_sources': len(attributions)
        }

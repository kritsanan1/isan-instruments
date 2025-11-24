import yt_dlp
from pathlib import Path
from typing import Dict, Optional
import json
from datetime import datetime


class YouTubeAudioDownloader:
    """
    Download audio from YouTube videos with proper attribution tracking
    Ensures ethical data collection for Thai music research
    """
    
    def __init__(self, output_dir: str = "data/raw"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def download_audio(self, url: str, 
                      instrument: str,
                      technique: Optional[str] = None,
                      attribution_notes: Optional[str] = None) -> Dict:
        """
        Download audio from YouTube with metadata tracking
        
        Args:
            url: YouTube video URL
            instrument: Instrument type (Phin, Khaen, etc.)
            technique: Playing technique/pattern (ลายพิณ)
            attribution_notes: Additional attribution information
        
        Returns:
            Dictionary with download info and file path
        """
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'wav',
                'preferredquality': '192',
            }],
            'outtmpl': str(self.output_dir / '%(title)s_%(id)s.%(ext)s'),
            'quiet': False,
            'no_warnings': False,
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                
                video_id = info['id']
                title = info['title']
                uploader = info.get('uploader', 'Unknown')
                upload_date = info.get('upload_date', 'Unknown')
                duration = info.get('duration', 0)
                view_count = info.get('view_count', 0)
                
                audio_file = self.output_dir / f"{title}_{video_id}.wav"
                
                metadata = {
                    'source': 'YouTube',
                    'url': url,
                    'video_id': video_id,
                    'title': title,
                    'uploader': uploader,
                    'upload_date': upload_date,
                    'duration': duration,
                    'view_count': view_count,
                    'instrument': instrument,
                    'technique': technique,
                    'attribution_notes': attribution_notes,
                    'downloaded_at': datetime.now().isoformat(),
                    'file_path': str(audio_file),
                    'consent_status': 'Public YouTube video - Fair use for research',
                    'ethical_notes': 'Downloaded for educational and cultural preservation purposes'
                }
                
                metadata_file = self.output_dir / f"{title}_{video_id}_metadata.json"
                with open(metadata_file, 'w', encoding='utf-8') as f:
                    json.dump(metadata, f, indent=2, ensure_ascii=False)
                
                return {
                    'success': True,
                    'file_path': str(audio_file),
                    'metadata': metadata,
                    'message': f'Successfully downloaded: {title}'
                }
        
        except Exception as e:
            return {
                'success': False,
                'error': str(e),
                'url': url,
                'message': f'Failed to download: {str(e)}'
            }
    
    def download_batch(self, video_list: list) -> list:
        """
        Download multiple videos in batch
        
        Args:
            video_list: List of dicts with 'url', 'instrument', 'technique', 'notes'
        
        Returns:
            List of download results
        """
        results = []
        
        for i, video_info in enumerate(video_list, 1):
            print(f"\n[{i}/{len(video_list)}] Processing: {video_info.get('url', 'Unknown URL')}")
            
            result = self.download_audio(
                url=video_info['url'],
                instrument=video_info.get('instrument', 'Unknown'),
                technique=video_info.get('technique'),
                attribution_notes=video_info.get('notes')
            )
            
            results.append(result)
            
            if result['success']:
                print(f"  ✓ {result['message']}")
            else:
                print(f"  ✗ {result['message']}")
        
        success_count = sum(1 for r in results if r['success'])
        print(f"\n{'='*60}")
        print(f"Batch download complete: {success_count}/{len(video_list)} successful")
        print(f"{'='*60}")
        
        return results
    
    def get_video_info(self, url: str) -> Dict:
        """Get video information without downloading"""
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
        }
        
        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=False)
                
                return {
                    'success': True,
                    'title': info['title'],
                    'uploader': info.get('uploader', 'Unknown'),
                    'duration': info.get('duration', 0),
                    'view_count': info.get('view_count', 0),
                    'description': info.get('description', '')[:200] + '...',
                    'upload_date': info.get('upload_date', 'Unknown')
                }
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }


def create_phin_video_list():
    """
    Create list of Phin tutorial/performance videos for batch download
    Based on the provided YouTube links
    """
    videos = [
        {
            'url': 'https://www.youtube.com/watch?v=ksZ3DWA9mPE',
            'instrument': 'Phin',
            'technique': 'Basic/Foundation',
            'notes': 'ดุลย์เพลงพิณ - Basic Phin teaching'
        },
        {
            'url': 'https://www.youtube.com/watch?v=ZRK75tNHqKc',
            'instrument': 'Phin',
            'technique': 'Phin Flow Technique',
            'notes': 'M MUSIC GROUP - Teaching Phin flow technique'
        },
        {
            'url': 'https://www.youtube.com/watch?v=aQZEN3y8zWo',
            'instrument': 'Phin',
            'technique': 'ลายมโหรีอีสาน',
            'notes': 'สตีฟ ฐิติวัสส์ - Mahori Isan pattern'
        }
    ]
    
    return videos

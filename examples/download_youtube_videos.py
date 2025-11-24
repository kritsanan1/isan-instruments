import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from src.data_collection.youtube_downloader import YouTubeAudioDownloader, create_phin_video_list
from src.models.dataset_manager import DatasetManager


def download_phin_tutorials():
    """
    Download Phin tutorial videos from YouTube for training data
    
    IMPORTANT ETHICAL NOTES:
    - These are publicly available educational videos
    - Downloaded for research and cultural preservation purposes
    - Proper attribution is maintained in metadata
    - For personal/educational use only
    """
    print("=" * 70)
    print("YOUTUBE PHIN TUTORIAL DOWNLOADER")
    print("=" * 70)
    print("\n⚠️  ETHICAL CONSIDERATIONS:")
    print("  - Videos are public educational content")
    print("  - Downloaded for research & cultural preservation")
    print("  - Full attribution maintained in metadata")
    print("  - For non-commercial educational use only")
    print("\nDo you want to proceed? (yes/no): ", end="")
    
    response = input().strip().lower()
    if response != 'yes':
        print("\nDownload cancelled.")
        return
    
    downloader = YouTubeAudioDownloader(output_dir="data/raw")
    video_list = create_phin_video_list()
    
    print(f"\n📋 Videos to download: {len(video_list)}")
    for i, video in enumerate(video_list, 1):
        print(f"  {i}. {video['technique']} - {video['notes']}")
    
    print(f"\n{'='*70}")
    print("Starting downloads...")
    print(f"{'='*70}")
    
    results = downloader.download_batch(video_list)
    
    successful_downloads = [r for r in results if r['success']]
    
    if len(successful_downloads) > 0:
        print(f"\n{'='*70}")
        print("ADDING TO DATASET")
        print(f"{'='*70}")
        
        dataset_manager = DatasetManager()
        
        for result in successful_downloads:
            metadata = result['metadata']
            
            try:
                rec_id = dataset_manager.add_recording(
                    file_path=metadata['file_path'],
                    instrument=metadata['instrument'],
                    technique=metadata['technique'] or 'Unknown',
                    performer_name=metadata['uploader'],
                    consent_status=True,
                    cultural_attribution=f"YouTube: {metadata['title']} by {metadata['uploader']}",
                    notes=f"YouTube video ID: {metadata['video_id']}. {metadata.get('attribution_notes', '')}"
                )
                print(f"  ✓ Added to dataset: {rec_id} - {metadata['title'][:50]}...")
            
            except Exception as e:
                print(f"  ✗ Failed to add {metadata['title'][:30]}...: {str(e)}")
        
        print(f"\n{'='*70}")
        print("DOWNLOAD & DATASET UPDATE COMPLETE")
        print(f"{'='*70}")
        print(f"\n✓ Successfully downloaded: {len(successful_downloads)}/{len(video_list)} videos")
        print(f"✓ Added to dataset with proper attribution")
        print(f"\n📁 Audio files saved to: data/raw/")
        print(f"📋 Metadata saved to: data/raw/*_metadata.json")
        
        print(f"\n💡 Next steps:")
        print(f"  1. Review downloaded audio quality")
        print(f"  2. Run: python train_model.py")
        print(f"  3. Test with new authentic Phin recordings!")
    
    else:
        print(f"\n❌ No videos were successfully downloaded")
        print(f"Please check your internet connection and YouTube availability")


def preview_video_info():
    """Preview information about videos without downloading"""
    print("=" * 70)
    print("YOUTUBE VIDEO INFORMATION PREVIEW")
    print("=" * 70)
    
    downloader = YouTubeAudioDownloader()
    video_list = create_phin_video_list()
    
    for i, video in enumerate(video_list, 1):
        print(f"\n[{i}/{len(video_list)}] Fetching info for: {video['url']}")
        
        info = downloader.get_video_info(video['url'])
        
        if info['success']:
            print(f"\n  Title: {info['title']}")
            print(f"  Uploader: {info['uploader']}")
            print(f"  Duration: {info['duration'] // 60}:{info['duration'] % 60:02d}")
            print(f"  Views: {info.get('view_count', 0):,}")
            print(f"  Upload Date: {info['upload_date']}")
            print(f"  Instrument: {video['instrument']}")
            print(f"  Technique: {video['technique']}")
        else:
            print(f"  ✗ Error: {info.get('error', 'Unknown error')}")


if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Download Phin tutorial videos from YouTube')
    parser.add_argument('--preview', action='store_true', help='Preview video info without downloading')
    
    args = parser.parse_args()
    
    if args.preview:
        preview_video_info()
    else:
        download_phin_tutorials()

from youtube_data import youtube_data_collection
from gemini_analysis import Gemini_Analysis, load_youtube_data
from gmail_sender import send_analysis_email, test_gmail

# Video IDs to track (add/remove as needed)
VIDEO_IDS = [
    "JgDNFQ2RaLQ",
    "dQw4w9WgXcQ"
    # Add more video IDs here
]

def main(send_email=True, recipient_email=None):
    youtube_data_collection(VIDEO_IDS)
    
    json_data = load_youtube_data('youtube_tracking.json')
    
    data_points = [len(data) for data in json_data.values()]
    
    if any(dp < 2 for dp in data_points):
        print("❌ Not enough data points for analysis. Please run tracking multiple times.")
        return
    
    
    analysis_file  = Gemini_Analysis(Json_path='youtube_tracking.json')
    
    
    if not analysis_file:
        print("❌ Analysis generation failed")
        return
    
    if send_email:
        print("\n📧 Sending email report...")
        if test_gmail():
            send_analysis_email(analysis_file, recipient_email)
        else:
            print("⚠️ Email sending skipped due to connection issues")
    
    print("\n🎉 Complete!")
    return analysis_file
        

if __name__ == "__main__":
    main(send_email=True)

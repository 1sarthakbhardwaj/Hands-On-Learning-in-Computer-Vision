import google.generativeai as genai
from dotenv import dotenv_values
import json
from datetime import datetime

# Load environment variables
API = dotenv_values('.env')
GEMINI_API_KEY = API['GEMINI_API_KEY']

# Configure the API key
genai.configure(api_key=GEMINI_API_KEY)

# Initialize the model
model = genai.GenerativeModel('gemini-2.0-flash-exp')

def load_youtube_data(filename):
    """Load YouTube tracking data from JSON file"""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: {filename} not found!")
        return None
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in {filename}")
        return None

def calculate_growth_metrics(data):
    """Calculate growth metrics for each video"""
    analysis_results = {}
    
    for video_id, tracking_data in data.items():
        if len(tracking_data) < 2:
            continue
            
        # Sort by timestamp to ensure chronological order
        sorted_data = sorted(tracking_data, key=lambda x: x['timestamp'])
        
        first_record = sorted_data[0]
        latest_record = sorted_data[-1]
        
        # Calculate time difference
        first_time = datetime.fromisoformat(first_record['timestamp'])
        latest_time = datetime.fromisoformat(latest_record['timestamp'])
        time_diff_hours = (latest_time - first_time).total_seconds() / 3600
        
        # Calculate growth metrics
        view_growth = latest_record['view_count'] - first_record['view_count']
        like_growth = latest_record['like_count'] - first_record['like_count']
        comment_growth = latest_record['comment_count'] - first_record['comment_count']
        
        # Calculate hourly growth rates
        view_rate = view_growth / time_diff_hours if time_diff_hours > 0 else 0
        like_rate = like_growth / time_diff_hours if time_diff_hours > 0 else 0
        comment_rate = comment_growth / time_diff_hours if time_diff_hours > 0 else 0
        
        analysis_results[video_id] = {
            'title': latest_record['title'],
            'channel': latest_record['channel_title'],
            'published_date': latest_record['published_at'],
            'tracking_period_hours': round(time_diff_hours, 2),
            'total_records': len(tracking_data),
            'metrics': {
                'view_growth': view_growth,
                'like_growth': like_growth,
                'comment_growth': comment_growth,
                'view_growth_per_hour': round(view_rate, 2),
                'like_growth_per_hour': round(like_rate, 2),
                'comment_growth_per_hour': round(comment_rate, 2)
            },
            'current_stats': {
                'views': latest_record['view_count'],
                'likes': latest_record['like_count'],
                'comments': latest_record['comment_count']
            }
        }
    
    return analysis_results

def create_analysis_prompt(analysis_data):
    """Create a comprehensive prompt for Gemini analysis"""
    
    # Convert analysis data to a readable format
    data_summary = "YouTube Video Analytics Data:\n\n"
    
    for video_id, info in analysis_data.items():
        data_summary += f"Video: {info['title']}\n"
        data_summary += f"Channel: {info['channel']}\n"
        data_summary += f"Video ID: {video_id}\n"
        data_summary += f"Published: {info['published_date']}\n"
        data_summary += f"Tracking Period: {info['tracking_period_hours']} hours\n"
        data_summary += f"Data Points Collected: {info['total_records']}\n"
        
        data_summary += "\nGrowth Metrics:\n"
        data_summary += f"- View Growth: {info['metrics']['view_growth']:,} ({info['metrics']['view_growth_per_hour']} per hour)\n"
        data_summary += f"- Like Growth: {info['metrics']['like_growth']:,} ({info['metrics']['like_growth_per_hour']} per hour)\n"
        data_summary += f"- Comment Growth: {info['metrics']['comment_growth']:,} ({info['metrics']['comment_growth_per_hour']} per hour)\n"
        
        data_summary += "\nCurrent Statistics:\n"
        data_summary += f"- Total Views: {info['current_stats']['views']:,}\n"
        data_summary += f"- Total Likes: {info['current_stats']['likes']:,}\n"
        data_summary += f"- Total Comments: {info['current_stats']['comments']:,}\n"
        data_summary += "\n" + "="*50 + "\n\n"
    
    prompt = f"""
    Analyze the following YouTube video tracking data and provide comprehensive insights:

    {data_summary}

    Please provide a detailed analysis covering:

    1. **Overall Performance Summary**
       - Which video is performing better and why?
       - Key performance indicators comparison

    2. **Growth Rate Analysis**
       - View growth patterns and rates
       - Engagement growth (likes and comments)
       - Growth velocity trends

    3. **Engagement Quality Assessment**
       - Like-to-view ratios
       - Comment-to-view ratios
       - Overall audience engagement quality

    4. **Content Performance Insights**
       - What factors might be contributing to the performance differences?
       - Age of content vs. performance correlation

    5. **Trend Predictions**
       - Based on current growth rates, what can we expect?
       - Recommendations for content strategy

    6. **Key Metrics Summary**
       - Most important takeaways
       - Action items based on the data

    Please provide specific numbers and percentages in your analysis, and format your response clearly with headings and bullet points where appropriate.
    """
    
    return prompt

def Gemini_Analysis(Json_path: str = 'youtube_tracking.json'):
    print("Loading YouTube tracking data...")
    
    # Load the YouTube data
    youtube_data = load_youtube_data('youtube_tracking.json')
    if not youtube_data:
        return
    
    print(f"Found {len(youtube_data)} videos in tracking data")
    
    # Calculate growth metrics
    print("Calculating growth metrics...")
    analysis_data = calculate_growth_metrics(youtube_data)
    
    if not analysis_data:
        print("No sufficient data for analysis (need at least 2 data points per video)")
        return
    
    # Create analysis prompt
    print("Preparing analysis prompt for Gemini...")
    analysis_prompt = create_analysis_prompt(analysis_data)
    
    # Generate analysis using Gemini
    print("Requesting analysis from Gemini API...")
    try:
        response = model.generate_content(analysis_prompt)
        
        print("\n" + "="*80)
        print("PERFORMING YOUTUBE ANALYTICS REPORT")
        print("="*80)
        
        # Save the analysis to a file
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        output_filename = f"youtube_analysis_{timestamp}.txt"
        
        with open(output_filename, 'w', encoding='utf-8') as f:
            f.write("YOUTUBE ANALYTICS REPORT\n")
            f.write("="*80 + "\n")
            f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write("\n\n" + "="*80 + "\n")
            f.write("GEMINI ANALYSIS:\n")
            f.write("="*80 + "\n")
            f.write(response.text)
        
        print(f"\nAnalysis saved to: {output_filename}")
        
    except Exception as e:
        print(f"Error generating analysis: {str(e)}")
        print("Please check your API key and internet connection.")
        
    return output_filename

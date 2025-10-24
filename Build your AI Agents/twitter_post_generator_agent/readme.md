# Twitter Post Generator Agent 🤖✨

[![Labellerr](https://img.shields.io/badge/Labellerr-BLOG-black.svg)](https://www.labellerr.com/blog/)
[![Youtube](https://img.shields.io/badge/Labellerr-YouTube-b31b1b.svg)](https://www.youtube.com/@Labellerr)
[![Github](https://img.shields.io/badge/Labellerr-GitHub-green.svg)](https://github.com/Labellerr/Hands-On-Learning-in-Computer-Vision)

An intelligent AI-powered system that automatically generates engaging Twitter/X posts from blog articles and YouTube videos using CrewAI and Google's Gemini models.

## 📋 Overview

This project implements a multi-agent workflow that extracts content from URLs (blogs or YouTube videos) and transforms them into viral-ready Twitter posts. The system uses two specialized AI agents working in sequence to deliver concise, engaging social media content with emojis, hashtags, and proper formatting.

### ✨ Key Features

- **Dual Content Support**: Extract content from both blog posts and YouTube videos
- **Intelligent Content Processing**: Automatic content extraction and summarization
- **Twitter-Optimized Output**: Generates posts within 280-character limit
- **Engaging Format**: Includes emojis, hashtags, and hooks for maximum engagement
- **Sequential Workflow**: Two-agent system for extraction and writing
- **Error Handling**: Robust error management for URL processing

### 🛠️ Tech Stack

- **CrewAI**: Multi-agent orchestration framework
- **Google Gemini**: Advanced LLM models (2.0-flash-exp & 2.5-flash)
- **BeautifulSoup4**: HTML parsing and web scraping
- **YouTube Transcript API**: Video transcript extraction
- **Python 3.10+**: Core programming language

## 📦 Prerequisites

Before running this project, ensure you have:

- Python 3.10 or higher installed
- A Google Gemini API key ([Get one here](https://makersuite.google.com/app/apikey))
- Basic understanding of Python and Jupyter notebooks
- Internet connection for content extraction

## 🚀 Installation

### Step 1: Clone the Repository

```bash
git clone <repository-url>
cd twitter-post-generator-agent
```

### Step 2: Create Virtual Environment

```bash
python -m venv agent
source agent/bin/activate  # On Windows: agent\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install crewai python-dotenv requests beautifulsoup4 youtube-transcript-api
```

### Step 4: Configure API Key

Create a `.env` file in the project root directory:

```bash
touch .env  # On Windows: type nul > .env
```

Add your Gemini API key to the `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

**Important**: Never commit your `.env` file to version control. Add it to `.gitignore`:

```bash
echo ".env" >> .gitignore
```

## 💻 Usage

### Running the Notebook

1. Launch Jupyter Notebook:
```bash
jupyter notebook main.ipynb
```

2. Execute cells sequentially from top to bottom

3. Modify the URL in the final execution cell:

```python
# For blog posts
url = "https://www.labellerr.com/blog/aios-explained/"

# For YouTube videos
url = "https://www.youtube.com/watch?v=GWB9ApTPTv4"

result = twitter_crew.kickoff(inputs={'url': url})
print(result.raw)
```

### Example Output

**Input**: Blog URL about AIOS (AI Agent Operating System)

**Output**:
```
Struggling with multi-agent AI? 🤯 AIOS (AI Agent Operating System) is your solution! 
It brings OS-level management to LLM-powered agents for scalable, collaborative AI.
🔗 https://www.labellerr.com/blog/aios-explained/
#AIOS #AIAutomation #MultiAgentAI #LLM #Tech
```

### Supported URL Formats

**Blog Posts**:
- Any standard HTTP/HTTPS web page with text content

**YouTube Videos**:
- `https://www.youtube.com/watch?v=VIDEO_ID`
- `https://youtu.be/VIDEO_ID`
- `https://www.youtube.com/embed/VIDEO_ID`
- `https://www.youtube.com/shorts/VIDEO_ID`
- `https://www.youtube.com/live/VIDEO_ID`

## 📁 Project Structure

```
twitter-post-generator-agent/
│
├── main.ipynb              # Main Jupyter notebook
├── .env                    # API keys (not in git)
├── .gitignore             # Git ignore file
├── README.md              # This file
└── requirements.txt       # Python dependencies
```

### Core Components

**1. Content Extraction Tools**
- `extract_content_from_url()`: Scrapes and parses blog content
- `extract_youtube_transcript()`: Fetches video transcripts

**2. AI Agents**
- **Content Extractor Agent**: Processes URLs and extracts key information
- **Twitter Writer Agent**: Creates engaging Twitter posts from extracted content

**3. LLM Configuration**
- **Extracting LLM**: Gemini 2.0 Flash (temperature: 0.1) for precise extraction
- **Writing LLM**: Gemini 2.5 Flash (temperature: 0.3) for creative output

## ⚙️ Configuration

### Adjusting LLM Parameters

Modify temperature settings for different output styles:

```python
# More deterministic output (0.0 - 0.3)
extracting_llm = LLM(model='gemini/gemini-2.0-flash-exp', 
                     apikey=GEMINI_API_KEY, 
                     temperature=0.1)

# More creative output (0.3 - 0.7)
writing_llm = LLM(model='gemini/gemini-2.5-flash', 
                  apikey=GEMINI_API_KEY, 
                  temperature=0.5)
```

### Customizing Agent Behavior

Modify agent goals and backstories in the Agent Definitions cell:

```python
twitter_writer_agent = Agent(
    role='Twitter/X Post Writer',
    goal='Your custom goal here',
    backstory='Your custom backstory here',
    llm=writing_llm,
    verbose=True
)
```

## 🐛 Troubleshooting

### Common Issues

**1. API Key Error**
```
Error: GEMINI_API_KEY not found
```
**Solution**: Ensure `.env` file exists with correct API key format

**2. Import Error**
```
ModuleNotFoundError: No module named 'crewai'
```
**Solution**: Install dependencies using `pip install -r requirements.txt`

**3. YouTube Transcript Unavailable**
```
ERROR: Could not retrieve transcript
```
**Solution**: Video may not have captions. Try a different video with available transcripts

**4. Content Extraction Failed**
```
ERROR extracting content: HTTPError
```
**Solution**: Check URL validity and internet connection. Some sites may block scraping

**5. Character Limit Exceeded**
```
Twitter post exceeds 280 characters
```
**Solution**: The agent should auto-correct. If not, adjust the prompt in `write_task`

## 🔧 Advanced Usage

### Creating Custom Tools

Add new content sources by creating custom tools:

```python
@tool('Custom Extractor')
def extract_custom_content(url: str) -> str:
    '''Your custom extraction logic'''
    # Implementation here
    return extracted_content
```

### Modifying Task Flow

Add additional tasks for more processing steps:

```python
analysis_task = Task(
    description='Analyze sentiment and key themes',
    expected_output='Sentiment analysis report',
    agent=analyzer_agent,
    context=[extract_task]
)
```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/YourFeature`
3. **Commit changes**: `git commit -m 'Add YourFeature'`
4. **Push to branch**: `git push origin feature/YourFeature`
5. **Open a Pull Request**

### Contribution Guidelines

- Follow PEP 8 style guidelines
- Add comments to complex code sections
- Update documentation for new features
- Test thoroughly before submitting PR

## 📝 License

This project is licensed under the MIT License. See LICENSE file for details.

## 📧 Contact & Support

- **Website**: [Labellerr](https://www.labellerr.com)
- **YouTube**: [@Labellerr](https://www.youtube.com/@Labellerr)
- **GitHub**: [Labellerr Organization](https://github.com/Labellerr)

For issues and feature requests, please open an issue on GitHub.

## 🙏 Acknowledgments

- CrewAI team for the amazing framework
- Google for Gemini API access
- Open-source community for essential libraries

## 📚 Additional Resources

- [CrewAI Documentation](https://docs.crewai.com/)
- [Google Gemini API Docs](https://ai.google.dev/docs)
- [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api)

---

**Made with ❤️ by Labellerr Team**

*Happy Tweet Generation! 🚀*
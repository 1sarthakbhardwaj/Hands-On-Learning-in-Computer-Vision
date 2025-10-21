# LinkedIn Post Generator Agent 🚀

> Transform your blog content into engaging LinkedIn posts automatically using AI-powered agents

An intelligent multi-agent system built with CrewAI that reads your blog posts and generates professional, engaging LinkedIn content optimized for maximum reach and engagement.

## ✨ Key Features

- **Automated Content Extraction**: Intelligently scrapes and cleans blog content from any URL
- **Two-Agent Workflow**: Specialized agents for content summarization and LinkedIn post creation
- **Smart Summarization**: Uses Gemini 2.0 Flash Lite to extract key points and insights
- **Creative Writing**: Leverages Gemini 2.5 Flash for compelling, engagement-optimized posts
- **Professional Formatting**: Includes emojis, hashtags, and clear CTAs
- **Industry Context**: Relates content to current trends and best practices
- **Character Optimized**: Generates posts within LinkedIn's optimal 180-word range

## 🛠️ Tech Stack

- **[CrewAI](https://www.crewai.com/)**: Multi-agent orchestration framework
- **[Google Gemini API](https://ai.google.dev/)**: Advanced LLM models for content processing
- **Beautiful Soup 4**: HTML parsing and content extraction
- **Python 3.8+**: Core programming language
- **python-dotenv**: Environment variable management

---

## 📋 Prerequisites

### Required Accounts & API Keys

1. **Google Gemini API Key**
   - Sign up at [Google AI Studio](https://makersuite.google.com/app/apikey)
   - Free tier available with generous limits
   - Required models: `gemini-2.0-flash-lite` and `gemini-2.5-flash`

### Software Requirements

- **Python**: Version 3.8 or higher
- **pip**: Latest version recommended
- **Internet connection**: Required for blog scraping and API calls

### System Requirements

- **OS**: Windows, macOS, or Linux
- **RAM**: Minimum 4GB
- **Storage**: ~500MB for dependencies

---

## 🔧 Installation

### 1. Clone or Download the Repository

```bash
git clone <repository-url>
cd linkedin-post-generator
```

### 2. Create a Virtual Environment

**Windows:**
```bash
python -m venv agent
agent\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv agent
source agent/bin/activate
```

### 3. Install Dependencies

```bash
pip install --upgrade pip
pip install crewai python-dotenv requests beautifulsoup4
pip install "crewai[tools]"
```

### 4. Configure API Keys

Create a `.env` file in the project root:

```bash
touch .env  # macOS/Linux
# or
type nul > .env  # Windows
```

Add your API key to `.env`:

```env
GEMINI_API_KEY=your_actual_api_key_here
```

**⚠️ Security Note**: Never commit your `.env` file to version control. Add it to `.gitignore`:

```bash
echo ".env" >> .gitignore
```

---

## 🚀 Usage

### Quick Start

1. **Open the Jupyter Notebook**:
```bash
jupyter notebook main.ipynb
```

2. **Run all cells sequentially** or execute the Python script directly:

```bash
python -c "from main import *; run_workflow()"
```

### Basic Example

```python
from dotenv import load_dotenv
from crewai import Crew, Process
import os

# Load environment
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Set your blog URL
BLOG_URL = "https://www.labellerr.com/blog/product-update-august-2025/"

# Run the crew
result = linkedin_writer_crew.kickoff(inputs={"blog_url": BLOG_URL})
print(result)
```

### Expected Output

The system generates a LinkedIn post with:

```
Tired of video annotations drifting off-sync? 😩

At Labellerr, we're thrilled to announce our latest release, 
bringing unparalleled precision to video annotation!

Here's what's new:
✨ Frame-Accurate Playback: Annotations stay perfectly synced
🎬 Intuitive Keyframe Management: Seamless timeline labeling
🚀 Smarter SAM2 Tracking: Faster workflows, lower costs

Ready to experience the difference?
Learn more: [Blog Link]

#DataAnnotation #AI #MachineLearning #ComputerVision
```

### Common Use Cases

1. **Content Marketing Teams**: Automate social media content from blog posts
2. **Developer Relations**: Share product updates and technical content
3. **SaaS Companies**: Promote feature releases and company news
4. **Personal Branding**: Convert blog articles into professional posts

---

## 📁 Project Structure

```
linkedin-post-generator/
│
├── main.ipynb              # Main Jupyter notebook with full workflow
├── .env                    # Environment variables (create this)
├── .env.example           # Example environment file
├── README.md              # This file
├── requirements.txt       # Python dependencies
│
└── outputs/               # (Optional) Generated posts directory
    └── posts/
```

### Key Files

- **`main.ipynb`**: Complete implementation with documentation cells
  - Content extraction logic
  - Agent definitions
  - Task configurations
  - Execution workflow

- **`.env`**: Stores sensitive API keys (not tracked in git)

- **`requirements.txt`**: All Python package dependencies

---

## ⚙️ Configuration

### Environment Variables

| Variable | Description | Required | Example |
|----------|-------------|----------|---------|
| `GEMINI_API_KEY` | Google Gemini API key | ✅ Yes | `AIzaSy...` |

### Agent Configuration

**Content Extractor Agent:**
```python
extracting_llm = LLM(
    model="gemini/gemini-2.0-flash-lite",
    api_key=GEMINI_API_KEY,
    temperature=0.1  # Lower for factual accuracy
)
```

**Post Writer Agent:**
```python
writing_llm = LLM(
    model="gemini/gemini-2.5-flash",
    api_key=GEMINI_API_KEY,
    temperature=0.2  # Higher for creativity
)
```

### Customization Options

**Adjust post length:**
```python
write_task = Task(
    description="Write a LinkedIn post (max 250 words)...",  # Change word count
    ...
)
```

**Modify tone:**
```python
writer_agent = Agent(
    backstory="Expert in casual, conversational B2C content...",  # Adjust tone
    ...
)
```

**Change content extraction depth:**
```python
def fetch_blog_content(url: str) -> str:
    return text[:6000]  # Increase from 4000 for longer blogs
```

---

## 🔍 Troubleshooting

### Common Errors

#### 1. **Missing API Key Error**
```
AssertionError: Missing GEMINI_API_KEY in .env
```
**Solution**: 
- Verify `.env` file exists in project root
- Check API key is correctly formatted: `GEMINI_API_KEY=your_key`
- Ensure no spaces around the `=` sign

#### 2. **Import Error: crewai not found**
```
ModuleNotFoundError: No module named 'crewai'
```
**Solution**:
```bash
pip install --upgrade crewai
pip install "crewai[tools]"
```

#### 3. **Rate Limit Exceeded**
```
Error 429: Too Many Requests
```
**Solution**:
- Wait 60 seconds and retry
- Check your [Gemini API quota](https://makersuite.google.com/)
- Consider upgrading to paid tier for higher limits

#### 4. **Content Extraction Fails**
```
ERROR fetching blog content: HTTPSConnectionPool
```
**Solution**:
- Verify the blog URL is accessible
- Check your internet connection
- Try with a different blog URL
- Some sites may block automated scraping - use official APIs when available

#### 5. **Beautiful Soup Warning**
```
UserWarning: No parser was explicitly specified
```
**Solution**:
```bash
pip install lxml
# Then modify: BeautifulSoup(resp.text, "lxml")
```

### Performance Issues

**Slow response times:**
- Gemini API calls can take 5-15 seconds
- Blog scraping depends on target site speed
- Consider caching frequently used blog content

**Agent not working as expected:**
- Review agent backstories and goals
- Adjust LLM temperature settings
- Increase context in task descriptions
- Check verbose output for debugging

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### How to Contribute

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit your changes**: `git commit -m 'Add amazing feature'`
4. **Push to the branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Code Style Guidelines

- Follow [PEP 8](https://pep8.org/) Python style guide
- Use meaningful variable names
- Add docstrings to functions
- Include comments for complex logic
- Update README if adding new features

### Pull Request Process

1. Ensure all tests pass (if applicable)
2. Update documentation for any changed functionality
3. Add your changes to a "Changelog" section
4. Request review from maintainers

### Ideas for Contributions

- 🎨 Add support for Twitter/X post generation
- 🌍 Multi-language support
- 📊 Analytics integration
- 🎯 A/B testing for post variations
- 📱 Web UI for easier access
- 🔧 Additional blog platform integrations

---

## 📄 License

This project is licensed under the **MIT License** - see below for details:

```
MIT License

Copyright (c) 2025 Labellerr

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## 🙏 Acknowledgments

### Frameworks & Tools

- **[CrewAI](https://www.crewai.com/)** - Multi-agent orchestration framework that makes AI collaboration seamless
- **[Google Gemini](https://ai.google.dev/)** - Powerful LLM models for content understanding and generation
- **[Beautiful Soup](https://www.cruxrepair.com/beautiful-soup-documentation)** - Elegant HTML/XML parsing library
- **[python-dotenv](https://github.com/theskumar/python-dotenv)** - Environment variable management

### Documentation & Resources

- [CrewAI Documentation](https://docs.crewai.com/)
- [Gemini API Documentation](https://ai.google.dev/docs)
- [LinkedIn Best Practices](https://business.linkedin.com/marketing-solutions/blog)

### Inspiration

This project was inspired by the need for efficient content repurposing in modern marketing workflows. Special thanks to the open-source community for making tools like these possible.

---

## 📧 Support

- **Issues**: [Open an issue](https://github.com/Labellerr/linkedin-post-generator/issues)
- **Documentation**: [View full docs](https://github.com/Labellerr/linkedin-post-generator/wiki)
- **Community**: [Join discussions](https://github.com/Labellerr/linkedin-post-generator/discussions)

---

**Made with ❤️ by [Labellerr](https://www.labellerr.com)** | [Blog](https://www.labellerr.com/blog/) | [YouTube](https://www.youtube.com/@Labellerr) | [GitHub](https://github.com/Labellerr)
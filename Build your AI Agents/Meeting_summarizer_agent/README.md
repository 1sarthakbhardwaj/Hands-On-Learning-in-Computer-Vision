# Meeting Summarizer Agent

This project implements an automated meeting summarization system. It takes an audio file, transcribes the speech to text using OpenAI's Whisper, and then uses Google's Gemini AI via CrewAI to generate a structured summary of the meeting.

## Features

- **Audio Transcription:** Accurately converts speech from an audio file into text using OpenAI's Whisper.
- **AI-Powered Summarization:** Generates a comprehensive summary including an overview, key discussion points, decisions made, action items, and open questions using Google's Gemini model.
- **Modular Design:** The system is broken down into a transcriber, a summarizer agent, and a complete pipeline for easy understanding and modification.
- **Output Saving:** Saves the full transcript and the generated summary to separate timestamped text files.

## Dependencies

The following packages are required to run the notebook:

- `openai-whisper`
- `crewai`
- `crewai-tools`
- `google-generativeai`
- `ffmpeg-python`

## Setup

1. **Install Dependencies:**

    ```bash
    pip install openai-whisper crewai crewai-tools google-generativeai ffmpeg-python
    ```

1. **Set up API Key:**
    - Create a file named `.env` in the root directory of the project.
    - Add your Gemini API key to the `.env` file as follows:

        ```env
        GEMINI_API_KEY="YOUR_API_KEY_HERE"
        ```

    - You can get a Gemini API key from [Google AI Studio](https://aistudio.google.com/app/apikey).

## Usage

1. Place your meeting audio file (e.g., `sample_audio.mp3`) in the project's root directory.
1. Open the `main.ipynb` notebook in a Jupyter environment.
1. In the final cell (cell #7), update the `AUDIO_FILE_PATH` variable to your audio file's name.

```python
# 7. USAGE
if __name__ == "__main__":
    AUDIO_FILE_PATH = "sample_audio.mp3"  # <-- Replace with your file!
    # ...
```

1. Run all the cells in the notebook from top to bottom.
1. The output will show the transcription and summarization process. The final transcript and summary will be printed in the notebook and saved to `meeting_transcript_YYYYMMDD_HHMMSS.txt` and `meeting_summary_YYYYMMDD_HHMMSS.txt` files respectively.

## How to Modify this Cookbook

This notebook is designed to be easily customizable. Here are a few ways you can modify it:

- **Change the Transcription Model:**
  You can use a different Whisper model for transcription by changing the `whisper_model` parameter during the `MeetingSummarizationPipeline` initialization. Available models are `tiny`, `base`, `small`, `medium`, and `large`. Larger models are more accurate but slower.

  ```python
  pipeline = MeetingSummarizationPipeline(
      whisper_model="small",  # Change model here
      gemini_api_key=GEMINI_API_KEY
  )
  ```

- **Customize the Summary Structure:**
  The prompt for the summarizer agent can be edited in the `summarize` method of the `MeetingSummarizerAgent` class. You can change the required sections (e.g., add "Next Steps" or remove "Open Questions") to better suit your needs.

  The `summarize` method in the `MeetingSummarizerAgent` class should be customized to include your desired sections:

  1. **Meeting Overview**: A brief, one-sentence summary
  2. **Key Topics**: Main subjects discussed
  ...- **Adjust the AI Model:**
  The Gemini model can be swapped out in the `MeetingSummarizerAgent` class. You can change the `model` name or adjust parameters like `temperature` for more or less creative responses.

  ```python
  # In class MeetingSummarizerAgent:
  def __init__(self, gemini_api_key=None):
      self.llm = LLM(
          model="gemini/gemini-pro",  # Change model here
          api_key=gemini_api_key,
          temperature=0.5
      )
  ```

- **Disable Saving Files:**
  If you only want to view the output within the notebook, you can disable file saving by setting `save_output=False` when calling the `process_meeting` method.

  ```python
  result = pipeline.process_meeting(
      audio_path=AUDIO_FILE_PATH,
      language="en",
      save_output=False  # Disable file output
  )
  ```
  
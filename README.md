# 🎬 YouTube Video Summarizer

A fun little Streamlit app that grabs YouTube transcripts and gets Google Gemini AI to sum it all up for you! 🚀

## ✨ Features

- 📝 Auto-fetches transcripts from YouTube videos.
- 🤖 Summarizes content using Gemini (Google AI) with the Agno agent.
- 🖥️ Super simple, interactive UI (thanks, Streamlit!).
- 🛠️ Add your own instructions and tools if you want.

## 🚀 Getting Started

### 🧰 What You’ll Need

- Python 3.8+
- [Streamlit](https://streamlit.io/)
- [youtube-transcript-api](https://github.com/jdepoix/youtube-transcript-api)
- [Agno](https://pypi.org/project/agno/)
- Google Gemini API key

### ⚡ Installation

1. **Clone this repo:**

```bash
git clone https://github.com/TheCarBun/YT-Vid-Summarizer.git
cd yt-vid-summarizer
```

2. **Install the goodies:**

```bash
pip install -r requirements.txt
```

3. **Add your secrets:**

Make a `.streamlit/secrets.toml` file and pop in your Gemini API key:

```toml
GEMINI_API_KEY = "your-gemini-api-key"
```

4. **Fire it up:**

```bash
streamlit run main.py
```

## 🎉 How to Use

1. Open the app in your browser (usually at `http://localhost:8501`).
2. Paste a YouTube video URL in the box.
3. Hit **Summarize**.
4. Chill for a sec while the magic happens!

## 🛠️ How It Works

- **Transcript Extraction:** Uses `youtube-transcript-api` to grab the transcript.
- **Summarization:** Gemini (via Agno) crunches the transcript and follows your instructions.
- **Display:** You get a neat markdown summary!

## 🗂️ Code Peek

- `main.py`: The main app (UI, transcript stuff, agent setup).
- `instructions.py`: Where your summarization instructions live.
- Uses Agno’s `Agent` to chat with Gemini and handle tools.

## 🐞 Troubleshooting

- **No transcript?** Some videos just don’t have them.
- **API errors?** Double-check your Gemini API key and quota.

## 📄 License

MIT License

## 🙏 Thanks To

- [Streamlit](https://streamlit.io/)
- [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api)
- [Agno](https://pypi.org/project/agno/)
- [Google Gemini](https://ai.google.dev/)

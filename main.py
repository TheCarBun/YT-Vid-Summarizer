# Use Proxy to hide IP. YT is blocking fetch requests since the requests are coming from a cloud provider

import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
from agno.agent import Agent
from agno.models.google import Gemini
from instructions import instructions

GEMINI_API_KEY = st.secrets["GEMINI_API_KEY"]


def get_transcript(video_id):
    print(">>> Transcript tool was called <<<")
    try:
        proxies = {
            'http': '101.251.204.174:8080',
            'https': '101.251.204.174:8080'
        }
        transcript_data = YouTubeTranscriptApi.get_transcript(
            video_id, proxies=proxies)

        full_text = " ".join([item['text'] for item in transcript_data])

        return full_text

    except Exception as e:
        print(f"An error occured: {e}")
        return "Error fetching transcripts"


def main():
    model = Gemini(
        id="gemini-2.0-flash",
        api_key=GEMINI_API_KEY
    )

    yt_tools = [get_transcript]

    agent = Agent(
        name="YTSummarizerAI",
        model=model,
        instructions=instructions,
        tools=yt_tools,
        show_tool_calls=True,
        read_chat_history=True,
        markdown=True,
        debug_mode=True
    )

    st.set_page_config(
        page_icon="❓",
        page_title="YT Vid Summarizer"
    )

    st.title("❓ YouTube Video Summarizer")
    prompt = st.text_input(
        "YouTube Video URL", placeholder="https://www.youtube.com/watch?v=...")
    button = st.button("Summarize")

    if prompt and button:
        with st.spinner("Fetching video transcripts and summarizing post..."):
            response = agent.run(prompt)
            st.markdown(response.content)
    elif button:
        st.info("YouTube video link pls 😑")


if __name__ == "__main__":
    main()

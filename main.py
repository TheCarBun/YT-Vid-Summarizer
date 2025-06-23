from youtube_transcript_api import YouTubeTranscriptApi
from agno.agent import Agent
from agno.models.google import Gemini
from instructions import instructions
import os
from dotenv import load_dotenv
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


def get_transcript(video_id):
    try:
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id)

        full_text = " ".join([item['text'] for item in transcript_data])

        return full_text

    except Exception as e:
        print(f"An error occured: {e}")
        return "Error fetching transcripts"


def main():
    model = Gemini(
        id="gemini-2.5-flash",
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

    # CLI
    while True:
        prompt = input("You: ")
        if prompt.lower().strip() == 'exit':
            break

        response = agent.run(prompt)
        print(response.content)


if __name__ == "__main__":
    main()

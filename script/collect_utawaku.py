import os
from dotenv import load_dotenv
from googleapiclient.discovery import build


load_dotenv()
api_key = os.getenv("API_KEY")

youtube = build("youtube", "v3", developerKey=api_key)
response = youtube.search().list(
    part="snippet",
    channelId="",  # TODO: Write channel ID
    maxResults=10,
    order="date",
    type="video",
).execute()

print(response)

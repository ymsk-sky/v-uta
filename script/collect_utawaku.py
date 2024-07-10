import json
import os
from datetime import datetime
from dotenv import load_dotenv
from googleapiclient.discovery import build


# dotenvで情報取得
load_dotenv()
api_key = os.getenv("API_KEY")
channel_id = os.getenv("CHANNEL_ID")

# タイムスタンプ取得
ts = datetime.now().strftime("%Y%m%d%H%M%S")

# YouTube APIで必要な情報を取得
utawaku = {}
youtube = build("youtube", "v3", developerKey=api_key)
page_token = ""
while 1:
    # 50件(Max)クエリ取得
    response = youtube.search().list(
        part="snippet",
        channelId=channel_id,  # channelId is read from dotfile
        maxResults=50,
        order="date",
        type="video",
        pageToken=page_token,
    ).execute()
    # 歌枠のみ取り出す
    for item in response["items"]:
        title = item["snippet"]["title"]
        if "歌枠" in title:
            video_id = item["id"]["videoId"]
            info = {
                "videoId": video_id,
                "url": f"https://www.youtube.com/watch?v={video_id}",
                "title": title,
                "date": item["snippet"]["publishedAt"],
            }
            utawaku[video_id] = info
            print(info)

    if "nextPageToken" in response:
        page_token = response["nextPageToken"]
    else:
        break

# 出力
with open(f"result_utawaku_{channel_id}_{ts}.json", mode="w", encoding="utf-8") as f:
    json.dump(utawaku, f, indent=4)

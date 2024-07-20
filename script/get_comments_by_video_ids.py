import json
import os
from datetime import datetime
import requests
from pathlib import Path
from dotenv import load_dotenv
from googleapiclient.discovery import build

URL = "https://www.googleapis.com/youtube/v3/commentThreads"


# dotenvで情報取得
load_dotenv()
api_key = os.getenv("API_KEY")
channel_id = os.getenv("CHANNEL_ID")

# タイムスタンプ取得
ts = datetime.now().strftime("%Y%m%d%H%M%S")

# 取得したvideoIdを読み込む
try:
    result_utawaku = sorted(list(Path(".").glob("./result_utawaku_*.json")))[-1]
except IndexError:
    print("No json file")
    exit()
with result_utawaku.open(mode="r") as f:
    utawaku = json.load(f)

# Ref: https://developers.google.com/youtube/v3/docs/commentThreads/list?hl=ja
youtube = build("youtube", "v3", developerKey=api_key)
# videoIdごとに処理
results = {}
for key in utawaku.keys():
    info = utawaku[key]
    video_id = info["videoId"]
    comments = []
    page_token = ""
    while 1:
        params = {
            "key": api_key,
            "part": "snippet",
            "videoId": video_id,
            "order": "relevance",
            "textFormat": "plainText",
            "maxResults": 50,
        }
        if page_token != "":
            params["pageToken"] = page_token
        response = requests.get(URL, params=params)
        resource = response.json()
        for comment_info in resource["items"]:
            comment = comment_info["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comments.append(comment)
            print(comment)

        if "nextPageToken" in resource:
            page_token = resource["nextPageToken"]
        else:
            break
    results[video_id] = comments
with open(f"result_comment_{channel_id}_{ts}.json", mode="w") as f:
    json.dump(results, f, indent=4)

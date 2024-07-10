import os
from dotenv import load_dotenv
from pathlib import Path

# dotenvで情報取得
load_dotenv()
channel_id = os.getenv("CHANNEL_ID")
vtuber = os.getenv("VTUBER")
agency = os.getenv("AGENCY")

files = list(Path(".").glob(f"result_preinfo_{channel_id}_*.csv"))
if len(files) == 0:
    print("No json files")
    exit()
file = files[0]

with open(file, mode="r", encoding="utf-8") as f:
    lines = f.readlines()

with open(f"data.csv", mode="w", encoding="utf-8") as f:
    for line in lines:
        _, ts, _, title, artist, video_id = line.strip().split(",")
        t = sum([int(v) * 60**k for k, v in enumerate(ts.split(":")[::-1])])
        url = f"https://youtu.be/{video_id}?t={t}"
        f.write(f"{title},{artist},{vtuber},{agency},{url}\n")

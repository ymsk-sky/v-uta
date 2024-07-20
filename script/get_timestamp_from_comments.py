import json
import os
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path


# dotenvで情報取得
load_dotenv()
channel_id = os.getenv("CHANNEL_ID")

# タイムスタンプ取得
ts = datetime.now().strftime("%Y%m%d%H%M%S")

files = list(Path(".").glob(f"result_comment_{channel_id}_*.json"))
if len(files) == 0:
    print("No json files")
    exit()
file = sorted(files)[-1]
with file.open(mode="r") as f:
    data = json.load(f)

results = {}
for video_id, comments in data.items():
    print(f"# {video_id}")
    # 長いコメント = セットリスト記述している可能性が高い
    candidates = [[c.replace("\r", "") for c in com.split("\n") if c != ""] for com in comments]
    result = max(candidates, key=lambda e: len(e))
    results[video_id] = result

with open(f"result_timestamp_{channel_id}_.json", mode="w") as f:
    json.dump(results, f, indent=4)

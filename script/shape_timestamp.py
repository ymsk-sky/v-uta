import json
import os
import re
from datetime import datetime
from dotenv import load_dotenv
from pathlib import Path

# dotenvで情報取得
load_dotenv()
channel_id = os.getenv("CHANNEL_ID")

# タイムスタンプ取得
ts = datetime.now().strftime("%Y%m%d%H%M%S")

files = list(Path(".").glob(f"result_timestamp_{channel_id}_*.json"))
if len(files) == 0:
    print("No json files")
    exit()
file = files[0]
with file.open(mode="r") as f:
    data = json.load(f)

with open(f"result_preinfo_{channel_id}_{ts}.csv", mode="w", encoding="utf-8") as f:
    for video_id, lines in data.items():
        print(f"# {video_id}")
        for line in lines:
            l = line.split()
            if len(l) < 2:
                continue
            src_e = ""
            stamp = "0"
            sec = 0
            for i, e in enumerate(l):
                # タイムスタンプなら秒に変換
                # タイムスタンプ以降が歌、歌手などの情報
                if ":" in e:
                    src_e = e
                    stamp = re.sub(r'[^0-9:]', "", e)
                    sec = sum([int(v) * 60**k for k, v in enumerate(stamp.split(":")[::-1])])
                    break
            else:
                i = -1
            info = " ".join(l[i + 1:])
            print(f"src:{src_e}, ts:{stamp}, sec:{sec}, info:{info}")
            f.write(f"{src_e},{stamp},{sec},{info},{video_id}\n")

import requests

file = "../script/data.csv"

with open(file, mode="r", encoding="utf-8") as f:
    lines = f.readlines()

for line in lines:
    song, artist, vtuber, agency, url = line.strip().split(",")
    data = {
        "song_title": song,
        "original_artist": artist,
        "vtuber_name": vtuber,
        "vtuber_agency": agency,
        "video_type": "utawaku",
        "urls": [url],
    }
    # POST
    response = requests.post("http://localhost:8000", json=data)
    if response.status_code == 200:
        print(f"fin {line}")
    else:
        print("Error")
        break

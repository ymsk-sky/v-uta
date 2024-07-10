# About script
YouTube Data APIを使って歌枠情報を取得し, そのコメント欄のタイムスタンプ情報を収集する.

## How to Use

`.env`に以下のパラメータを記述する.

```
API_KEY=
CHANNEL_ID=
```

* `API_KEY`は[Google Cloud プラットフォーム](https://console.cloud.google.com/?hl=ja)で確認可能
* `CHANNLE_ID`は[他人のYouTubeのチャンネルIDを調べる](https://ilr.jp/tech/485/)から取得可能

```shell
cd script
.venv/Script/activate

python collect_utawaku.py
# result_utawaku_{channel_id}_{timestamp}.jsonファイルが生成される

python get_comments_by_video_ids.py
# result_comment_{channel_id}_{timestamp}.jsonファイルが生成される

python get_timestamp_from_comments.py
# result_timestamp_{channel_id}_{timestamp}.jsonファイルが生成される

python shape_timestamp.py
# result_preinfo_{channel_id}_{timestamp}.csvファイルが生成される
```

## Details
- `collect_utawaku.py`: YouTube Data APIで対象チャンネルの"歌枠"の情報を収集してjson出力する

- `get_comments_by_video_ids.py`: 動画毎のコメント一覧を取得してjson出力する

- `get_timestamp_from_comments.py`: コメント一覧からタイムスタンプ情報を記述したコメントを抽出する

- `shape_timestamp.py`: タイムスタンプ情報を整形してcsvファイルに出力する

ここで出力されたcsvファイルの形式が以下の通り.

```csv
[生タイムスタンプ文字列],[不要文字削除したタイムスタンプ文字列],[タイムスタンプ秒数],[歌情報],[動画ID]
```

**生タイムスタンプ文字列は不要文字が紛れている可能性があり, 2つめのカラムのタイムスタンプが正しくないことがある. そのため目視確認後に手動で修正が必要**

**また, [歌情報]は[歌名],[歌手]の形式に手動で修正する必要あり**

- `make_records.py`: 上記csvファイルとチャンネルID等からデータベース登録に必要な情報を生成する

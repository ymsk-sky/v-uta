# v-uta
概要.

## プロジェクト作成時

```shell
npx create-next-app front --ts
```
- ESLint: Yes
- Tailwind CSS: No
- src directory: No
- App Router: Yes
- import alias: No

```shell
cd front
npm install @mui/material @emotion/react @emotion/styled
```

```shell
cd back
python -m venv .venv
.venv/Script/activate
python -m pip install --upgrade pip
pip install wheel
pip install fastapi, sqlalchemy
```

```shell
cd script
python -m venv .venv
.venv/Script/activate
python -m pip install --upgrade pip
pip install python-dotenv
pip install --upgrade google-api-python-client
```

## 動作

### フロントエンド

```shell
cd front
npm run dev
```

### バックエンド

```shell
cd back
.venv/Script/activate
fastapi dev main.py
```

### スクリプト

```shell
cd script
.venv/Script/activate
python collect_utawaku.py
```

#### 収集
`collect_utawaku.py`: YouTube Data APIで対象チャンネルの"歌枠"の情報を収集してjson出力する.

`.env`に以下のパラメータを記述する.

```
API_KEY=
CHANNEL_ID=
```

* `API_KEY`は[Google Cloud プラットフォーム](https://console.cloud.google.com/?hl=ja)で確認可能
* `CHANNLE_ID`は[他人のYouTubeのチャンネルIDを調べる](https://ilr.jp/tech/485/)から取得可能

### その他

nodeはvoltaで管理している.
バージョンは`18.20.3`(LTS).

pythonは3.10.xを想定.

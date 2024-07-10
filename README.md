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

[詳細](README_SCRIPT.md)

### その他

nodeはvoltaで管理している.
バージョンは`18.20.3`(LTS).

pythonは3.10.xを想定.

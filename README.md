# 📅 Discord Event Creator Bot from .ics

このBotは `.ics` ファイル（iCalendar形式）から Discord サーバー上のイベントを**まとめて自動作成**するツールです。学校の時間割、文化祭、サークル活動のスケジュールなど、iCalendar形式のデータをそのままDiscordに反映できます。

---

## 🛠 機能概要

- `.ics` ファイルからイベントを読み込み
- Discordの**スケジュールイベント**を自動作成
- 過去の日付のイベントは自動スキップ
- イベント名、開始・終了時刻、説明、場所を反映

---

## 📦 インストール

### 1. 仮想環境の作成（推奨）

```bash
python -m venv venv
source venv/bin/activate  # Windows の場合は venv\Scripts\activate
```

### 2. 必要なライブラリをインストール

```bash
pip install discord.py ics python-dotenv
```
またはrequirements.txt を使って
```bash
discord.py
ics
python-dotenv
```

## ⚙️ 設定ファイル
.env ファイルをプロジェクトのルートに作成し、以下のように設定します
```ini
DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN
GUILD_ID=YOUR_DISCORD_GUILD_ID
```

- DISCORD_TOKEN: Discord Developer Portal で取得したボットトークン
- GUILD_ID: イベントを作成する対象のサーバー（ギルド）のID

## 🧠 使用方法

### 1. sample.ics ファイル（または任意の .ics ファイル）を用意します。

### 2. Discord サーバー上でボットを起動して、次のコマンドを実行
```diff
!create_events
```

.ics ファイル内のイベントが読み込まれ、未来の日付のイベントのみが Discord に作成されます。

## ⚠️ 注意点
- ボットに スケジュールイベントの作成権限 があることを確認してください。
- Discordの仕様により、過去の日付のイベントは作成できません。
- Discordの使用により、100件より多くのイベントは作成できません。.icsファイルに100件より多くの項目がある場合、処理途中からイベント作製ができなくなります。
- .ics ファイルのフォーマットが正しくないと失敗します。


## 🧪 例: .ics ファイルの内容
```ics
BEGIN:VCALENDAR
BEGIN:VEVENT
SUMMARY:サンプルイベント
DTSTART;TZID=Asia/Tokyo:20250420T140000
DTEND;TZID=Asia/Tokyo:20250420T150000
LOCATION:理科室
DESCRIPTION:化学実験デモ
END:VEVENT
END:VCALENDAR
```


## 📂 ファイル構成
``` bash
.
├── bot.py              # メインのBotコード
├── sample.ics          # サンプルのiCalendarファイル
├── .env                # トークンなどの設定ファイル
├── requirements.txt    # 必要なパッケージ
└── README.md           # このファイル
```

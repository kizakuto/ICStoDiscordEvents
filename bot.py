import discord
from discord.ext import commands
from ics import Calendar
from dotenv import load_dotenv
import os
from datetime import datetime, timezone
import traceback

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
GUILD_ID = int(os.getenv("GUILD_ID"))

intents = discord.Intents.default()
intents.guilds = True
intents.messages = True
intents.message_content = True  # メッセージ内容読み取りが必要

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} でログインしました！")
    for guild in bot.guilds:
        print(f"サーバー '{guild.name}' に接続しました")

@bot.command()
async def create_events(ctx, ics_file: str = "sample.ics"):
    print("create_eventsコマンドが呼ばれました")
    try:
        with open(ics_file, "r", encoding="utf-8") as f:
            calendar = Calendar(f.read())

        guild = bot.get_guild(GUILD_ID)
        if not guild:
            await ctx.send("指定されたサーバーが見つかりません。")
            return

        count = 0
        for event in calendar.events:
            try:
                if event.begin.datetime < datetime.now(timezone.utc):
                    print(f"スキップ: {event.name} (開始日時が過去です)")
                    continue

                await guild.create_scheduled_event(
                    name=event.name or "イベント名なし",
                    start_time=event.begin.datetime.replace(tzinfo=timezone.utc),
                    end_time=event.end.datetime.replace(tzinfo=timezone.utc),
                    description=event.description or "",
                    location=event.location or "未指定",
                    entity_type=discord.EntityType.external,
                    privacy_level=discord.PrivacyLevel.guild_only
                )
                count += 1
            except Exception as e:
                print(f"イベント作成エラー: {e}")
                traceback.print_exc()
                continue

        await ctx.send(f"{count}件のイベントを作成しました！")
    except Exception as e:
        print(f"全体エラー: {e}")
        traceback.print_exc()
        await ctx.send("エラーが発生しました。")
        
bot.run(TOKEN)


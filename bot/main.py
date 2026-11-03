import asyncio
import sys

# Python 3.10+ & Pyrogram fix: Set event loop before any import
try:
    asyncio.get_event_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

# Ab yahan se apne baki imports shuru karein
from aiohttp import web
from pyrogram import Client
from config import config
from database import db
import asyncio
import os
from aiohttp import web
from pyrogram import Client
from config import config
from database import db

# Port configuration for Render
PORT = int(os.getenv("PORT", 8080))

# Initialize Pyrogram Bot Client
app_bot = Client(
    "neu_product_bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

async def main():
    # 1. Start Aiohttp Web Server for Render Keep-Alive / Health check
    web_app = web.Application()
    web_app.router.add_get("/", lambda r: web.json_response({"status": "alive", "bot": "NEU PRODUCT BOT"}))
    web_app.router.add_get("/health", lambda r: web.json_response({"status": "healthy"}))
    
    runner = web.AppRunner(web_app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", PORT)
    await site.start()
    print(f"🌐 Web server successfully listening on port {PORT}")

    # 2. Start Pyrogram Bot
    await app_bot.start()
    print("🤖 NEU PRODUCT BOT is online and running successfully!")
    
    # Keep the bot running
    await asyncio.Event().wait()

if __name__ == "__main__":
    # Python 3.10+ Event Loop fix for Render & Pyrogram
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    
    try:
        loop.run_until_complete(main())
    except KeyboardInterrupt:
        print("Bot stopped manually.")

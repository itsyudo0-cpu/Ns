import asyncio
import sys

# Python 3.10+ event loop fix for Pyrogram
try:
    asyncio.get_event_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

from pyrogram import Client, idle
# (Baki aapke baaki saare imports aur code iske baad aayenge)

"""
NEU PRODUCT BOT — Main Asynchronous Entrypoint
Runs the Pyrogram MTProto Bot Client concurrently with the aiohttp Keep-Alive & Webhook Server
on Render Free Web Service (PORT=8080).
Routes:
- GET /          -> 200 OK (UptimeRobot Keep-Alive)
- GET /health    -> 200 OK JSON Health Check
- POST /webhook/oxapay -> Instant OxaPay Crypto Payment Verification & Delivery
- POST /webhook/fampay -> Instant FamPay UPI Payment Verification & Delivery
"""
import asyncio
import json
import logging
from aiohttp import web
from pyrogram import Client, idle
from config import config
from database import db
from services.oxapay import OxaPayService
from services.fampay import FamPayService
from handlers.fsub import register_fsub_handlers
from handlers.admin import register_admin_handlers
from handlers.wallet import register_wallet_handlers
from handlers.user import register_user_handlers, deliver_order_payload

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)
logger = logging.getLogger("NEU_PRODUCT_BOT")

bot_app = Client(
    "neu_product_bot_session",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN,
    in_memory=True,
)


# -----------------------------------------------------------------------------
# AIOHTTP KEEP-ALIVE & WEBHOOK ROUTES (Render Free Web Service Port Binding)
# -----------------------------------------------------------------------------
async def handle_root(request: web.Request) -> web.Response:
    return web.Response(
        text="NEU PRODUCT BOT — Render 24/7 Keep-Alive & Webhook Server Active (200 OK)",
        status=200,
    )


async def handle_health(request: web.Request) -> web.Response:
    cfg = await db.get_settings()
    return web.json_response(
        {
            "status": "ok",
            "service": "NEU PRODUCT BOT",
            "maintenance_mode": cfg.get("maintenance_mode", False),
            "fsub_channels_count": len(cfg.get("fsub_channels", [])),
            "currencies": cfg.get("currencies", {}),
            "gateways": cfg.get("gateways", {}),
        },
        status=200,
    )


async def handle_oxapay_webhook(request: web.Request) -> web.Response:
    raw_body = await request.read()
    hmac_header = request.headers.get("hmac", "")

    if not OxaPayService.verify_webhook_signature(raw_body, hmac_header):
        logger.warning("Rejected OxaPay webhook: invalid HMAC signature")
        return web.json_response({"ok": False, "error": "Invalid signature"}, status=401)

    payload = json.loads(raw_body.decode("utf-8"))
    order_id = payload.get("orderId")
    status = payload.get("status", "").upper()

    if order_id and status in ("PAID", "COMPLETE", "CONFIRMED"):
        order = await db.get_order(order_id)
        if order and order.get("status") != "PAID":
            await db.update_order_status(order_id, "PAID")
            await deliver_order_payload(bot_app, order_id)
            logger.info(f"OxaPay Webhook: Delivered order {order_id}")

    return web.json_response({"ok": True}, status=200)


async def handle_fampay_webhook(request: web.Request) -> web.Response:
    raw_body = await request.read()
    sig_header = request.headers.get("X-FamPay-Signature", "")

    if not FamPayService.verify_webhook_signature(raw_body, sig_header):
        logger.warning("Rejected FamPay webhook: invalid signature")
        return web.json_response({"ok": False, "error": "Invalid signature"}, status=401)

    payload = json.loads(raw_body.decode("utf-8"))
    order_id = payload.get("txn_note") or payload.get("order_id")
    status = payload.get("status", "").upper()

    if order_id and status in ("SUCCESS", "PAID", "COMPLETED"):
        order = await db.get_order(order_id)
        if order and order.get("status") != "PAID":
            await db.update_order_status(order_id, "PAID")
            await deliver_order_payload(bot_app, order_id)
            logger.info(f"FamPay Webhook: Delivered order {order_id}")

    return web.json_response({"ok": True}, status=200)


async def start_services() -> None:
    logger.info("Initializing MongoDB Atlas collections & global_config...")
    await db.initialize()

    # Register modular Pyrogram handlers (FSub, Admin, Wallet, User)
    register_fsub_handlers(bot_app)
    register_admin_handlers(bot_app)
    register_wallet_handlers(bot_app)
    register_user_handlers(bot_app)

    # Start aiohttp Web Server on PORT (default 8080)
    web_app = web.Application()
    web_app.router.add_get("/", handle_root)
    web_app.router.add_get("/health", handle_health)
    web_app.router.add_post("/webhook/oxapay", handle_oxapay_webhook)
    web_app.router.add_post("/webhook/fampay", handle_fampay_webhook)

    runner = web.AppRunner(web_app)
    await runner.setup()
    site = web.TCPSite(runner, host="0.0.0.0", port=config.PORT)
    await site.start()
    logger.info(f"aiohttp Keep-Alive & Webhook server listening on port {config.PORT}")

    await bot_app.start()
    me = await bot_app.get_me()
    logger.info(f"NEU PRODUCT BOT started as @{me.username} (Owner ID: {config.OWNER_ID})")
    await idle()
    await bot_app.stop()
    await runner.cleanup()


if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    
    loop.run_until_complete(main())

async def main():
    # Aiohttp web server setup for Render port binding
    app = web.Application()
    app.router.add_get("/", lambda r: web.json_response({"status": "alive"}))
    app.router.add_get("/health", lambda r: web.json_response({"status": "alive"}))
    
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", PORT)
    await site.start()
    print(f"🌐 Web server listening on port {PORT}")

    # Start Pyrogram Bot
    await bot.start()
    print("🤖 NOHARA STORE BOT is online!")
    await asyncio.Event().wait()

if __name__ == "__main__":
    try:
        loop = asyncio.get_event_loop()
    except RuntimeError:
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
    
    loop.run_until_complete(main())

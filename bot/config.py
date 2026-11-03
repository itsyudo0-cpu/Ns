"""
NEU PRODUCT BOT — Global Configuration & Environment Loader
Optimized for Render Free Web Service + MongoDB Atlas + Telegram Channel Storage
"""
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # Telegram MTProto & Bot API Credentials
    API_ID: int = int(os.getenv("API_ID", "26944587"))
    API_HASH: str = os.getenv("API_HASH", "7261a455f2a6159b8a2fbfecd1a63004")
    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "9052932129:AAFMH0ywKmvArMWiUnrVIsiLjf5gE27WN0c")

    # Primary Owner Hierarchy (Strictly enforced for /addadmin, /removeadmin, /adminlist)
    OWNER_ID: int = int(os.getenv("OWNER_ID", "7955232487"))

    # MongoDB Atlas Async Connection URI
    MONGO_URI: str = os.getenv(
        "MONGO_URI",
        "mongodb+srv://kojar29650:h8jvNvpyteVB8AzM@cluster0.uywzxza.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
    )
    DB_NAME: str = os.getenv("DB_NAME", "neu_product_bot")

    # Telegram Channel Asset & Feedback Storage IDs
    DATABASE_CHANNEL_ID: int = int(os.getenv("DATABASE_CHANNEL_ID", "-1004396112942"))
    FEEDBACK_CHANNEL_ID: int = int(os.getenv("FEEDBACK_CHANNEL_ID", "-1004440712548"))
    LOG_CHANNEL_ID: int = int(os.getenv("LOG_CHANNEL_ID", "-1004396112942"))

    # Render Keep-Alive & Webhook HTTP Server
    PORT: int = int(os.getenv("PORT", "8080"))
    WEBHOOK_BASE_URL: str = os.getenv(
        "WEBHOOK_BASE_URL", "https://neu-product-bot.onrender.com"
    ).rstrip("/")

    # OxaPay Crypto Gateway Credentials
    OXAPAY_MERCHANT_API_KEY: str = os.getenv("OXAPAY_MERCHANT_API_KEY", "4WUA2N-O5OWXI-TOR7AB-APFYKD")
    OXAPAY_API_URL: str = "https://api.oxapay.com/merchants/request"

    # FamPay / UPI Dynamic QR & Webhook Credentials
    FAMPAY_MERCHANT_VPA: str = os.getenv("FAMPAY_MERCHANT_VPA", "Vickynohara@fam")
    FAMPAY_MERCHANT_NAME: str = os.getenv("FAMPAY_MERCHANT_NAME", "Vicky")
    FAMPAY_WEBHOOK_SECRET: str = os.getenv("FAMPAY_WEBHOOK_SECRET", "0x73ba57535e859238d4662bc4d98952d71aaca8c9")

    # Default Base Exchange Rate (Overridable dynamically in MongoDB settings)
    DEFAULT_USD_TO_INR: float = float(os.getenv("DEFAULT_USD_TO_INR", "97"))

    # Telegram Premium Custom Emoji IDs (Fallback-safe for standard & premium clients)
    EMOJI_SPARKLE = '<emoji id="5368324170671202286">✨</emoji>'
    EMOJI_WALLET = '<emoji id="5373141891321699086">👛</emoji>'
    EMOJI_CHECK = '<emoji id="5206607081334906820">✅</emoji>'
    EMOJI_ALERT = '<emoji id="5447644880824181073">⚠️</emoji>'
    EMOJI_CROWN = '<emoji id="5359785904535774578">👑</emoji>'
    EMOJI_FOLDER = '<emoji id="5397782960512444700">📁</emoji>'
    EMOJI_PACKAGE = '<emoji id="5463071033256848994">📦</emoji>'
    EMOJI_BOLT = '<emoji id="5330237710655306682">⚡️</emoji>'
    EMOJI_DIAMOND = '<emoji id="5472164874886846699">💎</emoji>'


config = Config()

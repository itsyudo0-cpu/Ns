LOCALES = {
    "en": {
        "welcome": "👋 <b>Welcome to NEU PRODUCT BOT!</b>\nSelect your preferred language and currency below:",
        "choose_currency": "💱 <b>Select your preferred currency:</b>",
        "main_menu": "🏠 <b>Main Dashboard</b>\nBrowse our digital catalog, check your wallet, or view past orders.",
        "catalog": "🛍 Catalog",
        "wallet": "👛 My Wallet",
        "orders": "📦 My Orders",
        "settings": "⚙️ Settings",
        "support": "📞 Support",
        "maintenance": "🛠 <b>Bot is currently under maintenance.</b> Please try again later.",
        "wallet_info": "👛 <b>Your Wallet Balance:</b> {balance}\n\nUse your balance for instant 1-click checkout!",
        "insufficient": "❌ Insufficient wallet balance! Please top up or use a direct payment gateway.",
        "order_delivered": "🎉 <b>Payment Verified!</b>\nYour product has been delivered above.\n🆔 Order ID: <code>{order_id}</code>",
        "leave_review": "⭐️ Leave a Review"
    },
    "hi": {
        "welcome": "👋 <b>NEU PRODUCT BOT में आपका स्वागत है!</b>\nनीचे अपनी भाषा और करेंसी चुनें:",
        "choose_currency": "💱 <b>अपनी पसंदीदा करेंसी चुनें:</b>",
        "main_menu": "🏠 <b>मुख्य मेनू</b>\nकैटलॉग देखें, अपना वॉलेट चेक करें या पुराने ऑर्डर्स देखें।",
        "catalog": "🛍 कैटलॉग",
        "wallet": "👛 मेरा वॉलेट",
        "orders": "📦 मेरे ऑर्डर्स",
        "settings": "⚙️ सेटिंग्स",
        "support": "📞 सहायता",
        "maintenance": "🛠 <b>बॉट अभी मेंटेनेंस में है।</b> कृपया कुछ देर बाद प्रयास करें।",
        "wallet_info": "👛 <b>आपका वॉलेट बैलेंस:</b> {balance}\n\nआप इस बैलेंस से तुरंत कोई भी प्रोडक्ट खरीद सकते हैं!",
        "insufficient": "❌ वॉलेट में पर्याप्त बैलेंस नहीं है! कृपया रिचार्ज करें या पेमेंट गेटवे चुनें।",
        "order_delivered": "🎉 <b>पेमेंट सफल रहा!</b>\nआपका प्रोडक्ट ऊपर भेज दिया गया है।\n🆔 ऑर्डर ID: <code>{order_id}</code>",
        "leave_review": "⭐️ रिव्यू दें"
    },
    "ru": {
        "welcome": "👋 <b>Добро пожаловать в NEU PRODUCT BOT!</b>\nВыберите язык и валюту:",
        "choose_currency": "💱 <b>Выберите предпочитаемую валюту:</b>",
        "main_menu": "🏠 <b>Главное меню</b>\nВыберите категорию, проверьте кошелек или заказы.",
        "catalog": "🛍 Каталог",
        "wallet": "👛 Кошелек",
        "orders": "📦 Мои заказы",
        "settings": "⚙️ Настройки",
        "support": "📞 Поддержка",
        "maintenance": "🛠 <b>Бот на техническом обслуживании.</b> Попробуйте позже.",
        "wallet_info": "👛 <b>Ваш баланс:</b> {balance}\n\nИспользуйте баланс для мгновенной покупки!",
        "insufficient": "❌ Недостаточно средств на балансе!",
        "order_delivered": "🎉 <b>Оплата подтверждена!</b>\nВаш товар доставлен выше.\n🆔 Заказ: <code>{order_id}</code>",
        "leave_review": "⭐️ Оставить отзыв"
    }
}

def t(lang: str, key: str, **kwargs) -> str:
    text = LOCALES.get(lang, LOCALES["en"]).get(key, LOCALES["en"][key])
    return text.format(**kwargs) if kwargs else text

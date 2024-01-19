import requests
import time
from telegram import Bot, ParseMode

# توکن ربات تلگرام 
TELEGRAM_BOT_TOKEN = 'YOUR_TELEGRAM_BOT_TOKEN'

# شناسه گروه تلگرامی
TELEGRAM_GROUP_ID = -100123456789  # Replace with your group ID

# آدرس API موردنظر
API_URL = 'https://api.nobitex.ir/v2/orderbook/USDTIRT'

def get_last_trade_price():
    try:
        response = requests.get(API_URL)
        data = response.json()
        last_trade_price = data['lastTradePrice']
        return last_trade_price
    except Exception as e:
        print(f"Error getting data from API: {e}")
        return None

def send_price_to_group(bot, group_id, price):
    try:
        message = f"Last Trade Price: {price} USDT/IRT"
        bot.send_message(chat_id=group_id, text=message, parse_mode=ParseMode.MARKDOWN)
        print("Price sent to the group.")
    except Exception as e:
        print(f"Error sending message to the group: {e}")

def main():
    # اتصال به ربات تلگرام
    bot = Bot(token=TELEGRAM_BOT_TOKEN)

    while True:
        # دریافت قیمت آخرین معامله
        last_trade_price = get_last_trade_price()

        if last_trade_price is not None:
            # ارسال قیمت به گروه تلگرامی
            send_price_to_group(bot, TELEGRAM_GROUP_ID, last_trade_price)

        # توقف برنامه برای ۳۰ دقیقه
        time.sleep(30 * 60)

if __name__ == "__main__":
    main()

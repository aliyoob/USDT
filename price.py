import telebot
import requests
TOKEN = "" // your bot token
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['usd'])
def usd(message):
    api_usd = "https://api.nobitex.ir/v2/orderbook/USDTIRT"
    price = requests.get(api_usd).json()
    price = price["lastTradePrice"]
    bot.reply_to(message, f"قیمت دلار: {price}")       
        
        
bot.infinity_polling()

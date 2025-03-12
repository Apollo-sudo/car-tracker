import telebot
from telebot import types

API_TOKEN = ''
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
async def send_welcome(message):
    markup = types.InlineKeyboardMarkup()
    button = types.InlineKeyboardButton(text="Открыть карту", url="")
    markup.add(button)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку ниже, чтобы открыть карту с твоим местоположением.", reply_markup=markup)

bot.polling()

# from telebot import types

# API_TOKEN = '8126643282:AAGmgnc56Qlm-E7pkBvWqAvu8SkZlmlX0OE'
# bot = telebot.TeleBot(API_TOKEN)

# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
#     button_geo = types.KeyboardButton(text="Отправить местоположение", request_location=True)
#     markup.add(button_geo)
#     bot.send_message(message.chat.id, "Привет! Отправь мне свою геолокацию, и я покажу её на карте. Ты также можешь поделиться своим местоположением в реальном времени.", reply_markup=markup)

# @bot.message_handler(content_types=['location'])
# def handle_location(message):
#     if message.location.live_period:
#         bot.reply_to(message, "Спасибо за то, что поделились своим местоположением в реальном времени!")
#     else:
#         latitude = message.location.latitude
#         longitude = message.location.longitude
#         bot.send_message(message.chat.id, f"Ваше местоположение: широта {latitude}, долгота {longitude}")
#         bot.send_location(message.chat.id, latitude, longitude)

# bot.polling()
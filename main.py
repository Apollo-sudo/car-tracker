import logging
import telebot
from telebot.types import ReplyKeyboardMarkup, KeyboardButton

bot = telebot.TeleBot(TOKEN)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Клавиатура с кнопкой запроса геолокации
location_keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
location_keyboard.add(KeyboardButton("📍 Отправить местоположение", request_location=True))

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привет! Нажми кнопку ниже, чтобы отправить своё местоположение.", reply_markup=location_keyboard)

@bot.message_handler(content_types=['location'])
def location_handler(message):
    lat = message.location.latitude
    lon = message.location.longitude
    bot.send_message(message.chat.id, f"Спасибо! Ваше местоположение:\nШирота: {lat}\nДолгота: {lon}")

if __name__ == "__main__":
    bot.polling(none_stop=True)

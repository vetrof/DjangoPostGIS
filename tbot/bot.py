# import logging
# import requests
# from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
# from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext
#
# # Токен для вашего Telegram-бота
# TELEGRAM_BOT_TOKEN = "6734627148:AAFu3cFheScfIIPNhQ38vmOJmGR5XwCLeZY"
# DJANGO_API_URL = "http://django_service:8000/api/coordinates"  # URL вашего Django API
#
# # Настройка логирования
# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#                     level=logging.INFO)
# logger = logging.getLogger(__name__)
#
# # Обработчик команды /start
# async def start(update: Update, context: CallbackContext):
#     keyboard = [
#         [KeyboardButton("Поделиться местоположением", request_location=True)]
#     ]
#     reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)
#     await update.message.reply_text('Привет! Поделитесь вашим местоположением, чтобы я мог помочь!', reply_markup=reply_markup)
#
# # Обработчик получения местоположения
# async def location(update: Update, context: CallbackContext):
#     user_location = update.message.location
#     lat = user_location.latitude
#     lng = user_location.longitude
#
#     # Делаем запрос к Django API
#     response = requests.get(DJANGO_API_URL, params={'lat': lat, 'lng': lng})
#
#     if response.status_code == 200:
#         data = response.json()
#         await update.message.reply_text(f"Информация: {data['message']}")
#     else:
#         await update.message.reply_text("Извините, не удалось получить данные.")
#
# # Основная функция для запуска бота
# def main():
#     application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()
#
#     # Обработчики команд
#     application.add_handler(CommandHandler("start", start))
#     application.add_handler(MessageHandler(filters.LOCATION, location))
#
#     # Запуск бота
#     application.run_polling()
#
# if __name__ == '__main__':
#     main()

import logging
import requests
from decouple import config
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

# Токен для вашего Telegram-бота
TELEGRAM_BOT_TOKEN = config("TELEGRAM_BOT_TOKEN")
API_URL = config("API_URL")


# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

# Обработчик команды /start
async def start(update: Update, context: CallbackContext):
    keyboard = [
        [KeyboardButton("Поделиться местоположением", request_location=True)]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True, resize_keyboard=True)
    await update.message.reply_text('Привет! Поделитесь вашим местоположением, чтобы я мог помочь!', reply_markup=reply_markup)

# Обработчик получения местоположения
async def location(update: Update, context: CallbackContext):
    user_location = update.message.location
    lat = user_location.latitude
    lon = user_location.longitude

    # Отправка координат на API
    response = requests.get(API_URL, params={'lat': lat, 'lon': lon})

    if response.status_code == 200:
        data = response.json()
        places = data.get('places', [])

        if places:
            # Формируем сообщение с информацией о местах
            message = "Ближайшие места:\n"
            for place in places:
                name = place['name']
                distance = place['distance_km']
                message += f"{name} - {distance:.2f} км\n"

            await update.message.reply_text(message)
        else:
            await update.message.reply_text("Не найдено ближайших мест.")
    else:
        await update.message.reply_text("Не удалось получить данные от API.")


# Основная функция для запуска бота
def main():
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Обработчики команд
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.LOCATION, location))

    # Запуск бота
    application.run_polling(poll_interval=0.5)

if __name__ == '__main__':
    main()

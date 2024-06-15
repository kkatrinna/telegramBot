import telebot
from telebot import types

bot = telebot.TeleBot('6337501489:AAHF7J0K1435ZBHr8IohegDWsIZ0S6DB3Hc')

logo = 'http://npcirs.ru/images/logo.png'

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton("Создание заявки")
    btn2 = types.KeyboardButton("Другой вопрос")
    btn3 = types.KeyboardButton("Контактная информация")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, text="НПЦ ИРС \n чем я могу Вам помочь?", reply_markup=markup)

bot.polling(none_stop=True, interval=0)

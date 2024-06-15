import telebot
from telebot import types

bot = telebot.TeleBot('6337501489:AAHF7J0K1435ZBHr8IohegDWsIZ0S6DB3Hc')

logo = 'http://npcirs.ru/images/logo.png'

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_photo(chat_id=message.chat.id, photo=logo)
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Создание заявки", callback_data="create_request")
    btn2 = types.InlineKeyboardButton("Другой вопрос", callback_data="other_question")
    btn3 = types.InlineKeyboardButton("Контактная информация", callback_data="contact_info")
    keyboard.add(btn1, btn2, btn3)

    bot.send_message(message.chat.id, text="НПЦ ИРС \n Чем я могу Вам помочь?", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == "create_request":
        bot.send_message(call.message.chat.id, "Вы нажали на кнопку 'Создание заявки'")
    elif call.data == "other_question":
        bot.send_message(call.message.chat.id, "Пожалуйста, задайте Ваш вопрос")
    elif call.data == "contact_info":
        bot.send_message(call.message.chat.id, f"Тел.: (495)330-07-88\n"
                                               f"Факс: (495)330-56-01\n"
                                               f"Телефон горячей линии: 8-800-100-40-90\n"
                                               f"E-mail: npcirs '@npcirs.ru'\n"
                                               f"Адрес главного офиса: 117393, г. Москва, ул. Профсоюзная, д. 78, стр. 1; этаж 8\n")
bot.polling(none_stop=True, interval=0)

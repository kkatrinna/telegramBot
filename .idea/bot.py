import telebot
from telebot import types

bot = telebot.TeleBot('6337501489:AAHF7J0K1435ZBHr8IohegDWsIZ0S6DB3Hc')

logo = 'http://npcirs.ru/images/logo.png'

user_data = {}

@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("Создание заявки", callback_data="create_request")
    btn2 = types.InlineKeyboardButton("Другой вопрос", callback_data="other_question")
    btn3 = types.InlineKeyboardButton("Контактная информация", callback_data="contact_info")
    keyboard.add(btn1, btn2, btn3)

    bot.send_message(message.chat.id, text="НПЦ ИРС \n Чем я могу Вам помочь?", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == "create_request":
        bot.send_message(call.message.chat.id, "Пожалуйста, напишите Ваше ФИО")
        bot.register_next_step_handler(call.message, get_surname)
    elif call.data == "other_question":
        bot.send_message(call.message.chat.id, "Пожалуйста, задайте Ваш вопрос")
    elif call.data == "contact_info":
        bot.send_message(call.message.chat.id, f"Тел.: (495)330-07-88\n"
                                               f"Факс: (495)330-56-01\n"
                                               f"Телефон горячей линии: 8-800-100-40-90\n"
                                               f"E-mail: npcirs@npcirs.ru\n"
                                               f"Адрес главного офиса: 117393, г. Москва, ул. Профсоюзная, д. 78, стр. 1; этаж 8\n")
def get_surname(message):
    user_data['surname'] = message.text
    bot.send_message(message.chat.id, "Укажите ВК")
    bot.register_next_step_handler(message, get_vk)
def get_vk(message):
    user_data['vk'] = message.text
    bot.send_message(message.chat.id, "Укажите ЗАВ№")
    bot.register_next_step_handler(message, get_numzav)
def get_numzav(message):
    user_data['numzav'] = message.text
    bot.send_message(message.chat.id, "Опишите Вашу проблему")
    bot.register_next_step_handler(message, get_description)
def get_description(message):
    user_data['description'] = message.text
    bot.send_message(message.chat.id, "Отправьте фото проблемы")
    bot.register_next_step_handler(message, get_photo)
def get_photo(message):
    user_data['photo'] = message.text
    bot.send_message(message.chat.id, "Теперь укажите Ваш номер телефона")
    bot.register_next_step_handler(message, get_phone)
def get_phone(message):
    user_data['email'] = message.text
    bot.send_message(message.chat.id, "Укажите Вашу почту")
    bot.register_next_step_handler(message, get_email)
def get_email(message):
    user_data['email'] = message.text
    bot.send_message(message.chat.id, f"Спасибо! Ваши данные: \nФамилия: {user_data['surname']}\nТелефон: {user_data['phone']}")

bot.polling(none_stop=True, interval=0)

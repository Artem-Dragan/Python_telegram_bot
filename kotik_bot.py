import telebot
from telebot import types
bot = telebot.TeleBot('5717706673:AAHX_XKbx-fPbbig-1wtuJuD9qjy6UFZmds')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = types.KeyboardButton('/bing')
    btn2 = types.KeyboardButton('/fin')
    btn3 = types.KeyboardButton('/soccer')
    btn4 = types.KeyboardButton('/kino')
    markup.add(btn1, btn2, btn3, btn4)
    mess = f'Привет {message.from_user.first_name}'
    bot.send_message(message.chat.id, mess, reply_markup=markup)

@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Вау, крутое фото!')

@bot.message_handler(commands=['bing'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("посетить сайт openAI", url = "bing.com"))
    bot.send_message(message.chat.id, 'зайди на сайт, нажав на кнопку ниже', reply_markup=markup)

@bot.message_handler(commands=['fin'])
def link(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('посетить сайт yahoo', url = 'https://finance.yahoo.com'))
    bot.send_message(message.chat.id, 'зайди на сайт с котировками, нажав на кнопку ниже', reply_markup=markup)

@bot.message_handler(commands=['soccer'])
def link2(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Сайт', url = 'https://soccer365.ru'))
    bot.send_message(message.chat.id, 'зайди на сайт футбола, нажав на кнопку ниже', reply_markup=markup)

@bot.message_handler(commands=['kino'])
def link3(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Сайт', url = 'https://kinopoisk.ru'))
    bot.send_message(message.chat.id, 'зайди на сайт с фильмами, нажав на кнопку ниже', reply_markup=markup)

# @bot.message_handler(content_types=['text'])
# def text(message):
#     if message.text == 'gpt':
#         def website(message):
#             markup = types.InlineKeyboardMarkup()
#             markup.add(types.InlineKeyboardButton("посетить сайт c openAI", url="bing.com"))
#             bot.send_message(message.chat.id, 'посетить сайт c openAI', reply_markup=markup)


@bot.message_handler()
def get_user_text(message):
    if message.text == "gpt":
        bot.send_message(message.chat.id, "click here <a href = 'https://chat.openai.com/auth/login'>openai</a>")
    elif message.text == "id":
        bot.send_message(message.chat.id, f'Твой ID: {message.from_user.id}')
    elif message.text == "hello":
        bot.send_message(message.chat.id, 'и тебе привет!')
    elif message.text == "photo":
        photo = open('photo_grey_cat.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, 'я тебя не понимать, набери: /start')

bot.polling(none_stop=True)


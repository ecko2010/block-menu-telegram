import telebot
from telebot import types
import random

TOKEN = '...'
bot = telebot.TeleBot(TOKEN)


# Обработчик на команду "старт"
@bot.message_handler(commands=['start'])
def start(message):
    # resize_keybord = True - чтобы размеры кнопок менялись в зависимости от экрана
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Рандомное число')
    item2 = types.KeyboardButton('Курсы валют')
    item3 = types.KeyboardButton('Информация')
    item4 = types.KeyboardButton('Другое')
    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id,'Здравствуй, {0.first_name}!'.format(message.from_user), reply_markup = markup)


# Обработчик на команду "Рандомное число"
@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'Рандомное число':
            bot.send_message(message.chat.id,'Ваше число: ' + str(random.randint(0,10000)))

        # Обработчик на команду "Курсы валют"
        elif message.text == 'Курсы валют':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.InlineKeyboardButton('USD Курс Доллара')
            item2 = types.KeyboardButton('EUR Курс Евро')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, back)

            bot.send_message(message.chat.id,'Выберите нужную Вам валюту', reply_markup = markup)

        # Обработчик на команду "Информация"
        elif message.text == 'Информация':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.InlineKeyboardButton('Что умеет бот')
            item2 = types.KeyboardButton('Кто создатель? Миссия?')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, back)

            bot.send_message(message.chat.id,'Информация', reply_markup = markup)

        # Обработчик на команду "Другое"
        elif message.text == 'Другое':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.InlineKeyboardButton('Настройки')
            item2 = types.KeyboardButton('Полезные советы')
            item3 = types.KeyboardButton('Стикер')
            back = types.KeyboardButton('Назад')
            markup.add(item1, item2, item3, back)

            bot.send_message(message.chat.id,'Другое', reply_markup = markup)
        
        # Кнопка "Назад"
        elif message.text == 'Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('Рандомное число')
            item2 = types.KeyboardButton('Курсы валют')
            item3 = types.KeyboardButton('Информация')
            item4 = types.KeyboardButton('Другое')
            markup.add(item1, item2, item3, item4)

            bot.send_message(message.chat.id,'Вы вернулись на главное меню', reply_markup = markup)

        # Кнопка "Стикер"
        elif message.text == 'Стикер':
            sticker = open('static/sticker.webp', 'rb')
            bot.send_sticker(message.chat.id, sticker)


# Чтобы бот не отключался 
bot.polling(none_stop=True)
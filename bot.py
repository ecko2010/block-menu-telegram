import telebot
from telebot import types
import random

TOKEN = '1709981956:AAFuOu2bGcD0CriK8gwjzO6VQVm8i0pO_VI'
bot = telebot.TeleBot(TOKEN)


# Handler for the "start" command
@bot.message_handler(commands=['start'])
def start(message):
    # resize_keybord = True - so that the button sizes change depending on the screen
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('random number')
    item2 = types.KeyboardButton('Exchange rates')
    item3 = types.KeyboardButton('Information')
    item4 = types.KeyboardButton('Other')
    markup.add(item1, item2, item3, item4)

    bot.send_message(message.chat.id,'Hello, {0.first_name}!'.format(message.from_user), reply_markup = markup)


# Handler for the command "Random number"
@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == 'random number':
            bot.send_message(message.chat.id,'your number: ' + str(random.randint(0,10000)))

        # Handler for the command "Currency rates"
        elif message.text == 'Exchange rates':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.InlineKeyboardButton('USD exchange rate')
            item2 = types.KeyboardButton('EUR exchange rate')
            back = types.KeyboardButton('Back')
            markup.add(item1, item2, back)

            bot.send_message(message.chat.id,'Choose the currency you need', reply_markup = markup)

        # Handler for the "Information" command
        elif message.text == 'Information':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.InlineKeyboardButton('What can a bot do')
            item2 = types.KeyboardButton('Who is the creator? Mission?')
            back = types.KeyboardButton('Back')
            markup.add(item1, item2, back)

            bot.send_message(message.chat.id,'Information', reply_markup = markup)

        # Handler for "Other" command
        elif message.text == 'Other':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.InlineKeyboardButton('Settings')
            item2 = types.KeyboardButton('Helpful Hints')
            item3 = types.KeyboardButton('Sticker')
            item4 = types.KeyboardButton('File')
            back = types.KeyboardButton('Back')
            markup.add(item1, item2, item3, item4, back)

            bot.send_message(message.chat.id,'Other', reply_markup = markup)
        
        # Back button
        elif message.text == 'Back':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('random number')
            item2 = types.KeyboardButton('Exchange rates')
            item3 = types.KeyboardButton('Information')
            item4 = types.KeyboardButton('Other')
            markup.add(item1, item2, item3, item4)

            bot.send_message(message.chat.id,'You have returned to the main menu', reply_markup = markup)

        # Sticker button
        elif message.text == 'Sticker':
            sticker = open('static/sticker.webp', 'rb')
            bot.send_sticker(message.chat.id, sticker)
            
         # File button getFile
       elif message.text == 'File':


# So that the bot does not turn off
bot.polling(none_stop=True)

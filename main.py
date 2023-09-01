
import telebot
from telebot import types

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot = telebot.TeleBot('6237784311:AAHi61AAQow_XNX74pyx9HGm5B4IHO2YZ5M')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('/command1')
    itembtn2 = types.KeyboardButton('/command2')
    markup.add(itembtn1, itembtn2)
    bot.send_message(message.chat.id, "Welcome to the bot! Please select a command:", reply_markup=markup)

@bot.message_handler(commands=['command1'])
def handle_command1(message):
    bot.send_message(message.chat.id, "Command 1 executed!")

@bot.message_handler(commands=['command2'])
def handle_command2(message):
    bot.send_message(message.chat.id, "Command 2 executed!")

bot.polling()

import os
from math import*
from cmath import *
import telebot
from logs import *


TOKEN = '5643113397:AAH8uR6e4cyQMI83U2AI-Cz4qZaU3pvmByU'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_hello(message):
    bot.reply_to(message, 'Калькулятор запущен, можно вводить выражение')

@bot.message_handler(func = lambda m: True)
def echo_all(message):
    
    text = message.text.replace("«", "'")
    text = text.replace("»", "'")
    try:  
        result = eval(text) 
        bot.reply_to(message, "Ответ: " + str(result))
        log(message, result)
    except SyntaxError:
        bot.reply_to(message, "Что то не так ввели")
    except: 
        bot.reply_to(message, "Попробуй еще раз!")

    
    
bot.infinity_polling()


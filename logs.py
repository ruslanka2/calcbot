from datetime import datetime as dt
from cal import *
from math import*
from cmath import *
from telebot import *




def log(message, result):
    dtime = dt.now()
    with open('log.json', 'a', encoding='utf-8') as file:
        file.write('{}; операция: {}; результат: {}\n'
                     .format(dtime, message.text, result))
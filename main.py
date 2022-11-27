import telebot
from telebot import TeleBot
from addition_calc import addition
from substraction_calc import subtraction
from myltiplication_calc import multiplication
from division_calc import division
from log import log


bot = TeleBot('5695846553:AAEIGlDzoxgHc1FoAa5b3o7sDFwv1C7Wrkg')

@bot.message_handler(commands=['start'])
def first_message(message):
    bot.send_message(message.chat.id,
                     text=(f'Это калькулятор, который считает рациональные и комплексные числа.\n'
                           'Для выполнения операций введите числа через пробел.\n'
                           'Например, для рациональных чисел "55 178" для выполнения команды "55+178"\n'
                           'Или "24 14j 112 5j" для выполнения команды "(24+14j)+(112+5j)".\n'
                           'Нже приведен список команд, которые может выполнять калькулятор\n'
                           '\n'
                           '/start - запуск программы\n'
                           '/addition - сложение\n'
                           '/subtraction - вычитание\n'
                           '/multiplication - умножение\n'
                           '/division - деление\n'
                           '/logs - запись операций\n'))


@bot.message_handler(commands=['addition'])
def additions(message: telebot.types.Message):
    bot.send_message(chat_id=message.from_user.id, text='Вы выбрали операцию сложения - введите через пробел числа')
    bot.register_next_step_handler(callback=addition_result_send, message=message)


def addition_result_send(message: telebot.types.Message):
    bot.send_message(chat_id=message.from_user.id, text=addition(message.text))
    log(message.text, 'addition', addition(message.text))


@bot.message_handler(commands=['subtraction'])
def subtractions(message: telebot.types.Message):
    bot.send_message(chat_id=message.from_user.id, text='Вы выбрали операцию вычитания - введите через пробел числа')
    bot.register_next_step_handler(callback=subtraction_result_send, message=message)


def subtraction_result_send(message: telebot.types.Message):
    bot.send_message(chat_id=message.from_user.id, text=subtraction(message.text))
    log(message.text, 'subtraction', subtraction(message.text))


@bot.message_handler(commands=['multiplication'])
def multiplications(message: telebot.types.Message):
    bot.send_message(chat_id=message.from_user.id, text='Вы выбрали операцию умножения - введите через пробел числа')
    bot.register_next_step_handler(callback=multiplication_result_send, message=message)


def multiplication_result_send(message: telebot.types.Message):
    bot.send_message(chat_id=message.from_user.id, text=multiplication(message.text))
    log(message.text, 'multiplication', multiplication(message.text))


@bot.message_handler(commands=['division'])
def division(message: telebot.types.Message):
    bot.send_message(chat_id=message.from_user.id, text='Вы выбрали операцию деления - введите через пробел числа')
    bot.register_next_step_handler(callback=division_result_send, message=message)


def division_result_send(message: telebot.types.Message):
    bot.send_message(chat_id=message.from_user.id, text=division(message.text))
    log(message.text, 'division', division(message.text))


@bot.message_handler(commands=['log'])
def bot_log(message: telebot.types.Message):
    bot.send_message(chat_id=message.from_user.id,
                     text='Список операций')
    bot.send_document(chat_id=message.from_user.id, document=open('results.txt', 'rb'))


bot.polling()

import telebot
import env_vars
from telebot import types


bot = telebot.TeleBot(env_vars.api_tok)

markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
btn_yes = types.KeyboardButton('Да')
btn_no = types.KeyboardButton('Нет')
btn_know = types.KeyboardButton('Пока не знаю')
markup_menu.add(btn_yes, btn_no, btn_know)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Привет, сегодня тренировка, придешь?", reply_markup=markup_menu)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text == 'Да':
        bot.reply_to(message, 'Отлично! Не опаздываем!', reply_markup=markup_menu)
    elif message.text == 'Нет':
        bot.reply_to(message, 'Ну вот : ( В следующий раз обязательно приходи!')
    elif message.text == 'Пока не знаю':
        bot.reply_to(message, 'Хорошо, как узнаешь дай знать!', reply_markup=markup_menu)
    else:
        bot.reply_to(message, 'Неправльная команда.')



bot.polling()

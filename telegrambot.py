import telebot
from telebot import types
import time
import schedule
import requests


bot_token = ''
bot_chatID = ''
bot = telebot.TeleBot(bot_token)
markup_menu = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
btn_yes = types.KeyboardButton('+')
btn_no = types.KeyboardButton('-')
btn_know = types.KeyboardButton('Пока не знаю')
markup_menu.add(btn_yes, btn_no, btn_know)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    players_going_to_come = 0
    if message.text == '+':
        players_going_to_come += 1
        bot.reply_to(message, str(players_going_to_come) + ' is going to come today.')


def telegram_bot_sendtext(bot_message):
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()


def report():
    my_message = "Всем привет, сегодня тренировка! Кто придет ставим плюсы! Кто нет - минусы."
    telegram_bot_sendtext(my_message)

bot.polling()
# schedule.every(.1).minutes.do(report)

# while True:
#     schedule.run_pending()
#     time.sleep(1)
    




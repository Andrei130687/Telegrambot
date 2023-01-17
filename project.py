import requests
import telebot
import random
from bs4 import BeautifulSoup
url = 'https://www.anekdot.ru/'
botanekdot = '5885954704:AAFCybJYfrIfpyfjDoR6tU6aJNVfVl8EU4s'
def parser(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    anekdot = soup.find_all('div', class_='text')
    return [i.text for i in anekdot ]

list_anekdot = parser(url)
random.shuffle(list_anekdot)
bot = telebot.TeleBot(botanekdot)
@bot.message_handler(commands=['start'])
def hello(message):
    bot.send_message(message.chat.id, 'Здравствуйте чтобы посмеяться введите цифру:')
@bot.message_handler(content_types=['text'])
def joke(message):
    if message.text.lower() in '123456789':
        bot.send_message(message.chat.id, list_anekdot[0])
        del list_anekdot[0]
    else:
        bot.send_message(message.chat.id, 'Введите любую цифру')
bot.polling()

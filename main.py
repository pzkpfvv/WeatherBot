import telebot
import config
import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.gismeteo.ru/weather-ulyanovsk-4407/')
html = BeautifulSoup(r.content, 'html.parser')
bot = telebot.TeleBot(config.TOKEN)


for el in html.select('#content'):
    t_min = el.select('.temperature .min')[0].text
    t_max = el.select('.temperature .max')[0].text


@bot.message_handler(content_types=['text'])
def welcome(message):
    bot.send_message(message.chat.id, "Привет, узнаем какая погода нас ожидает?")


    #keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Погода на сегодня")
    item2 = types.KeyboardButton("Неважно, как дела?)")

markup.add(item1, item2)


@bot.message_handler(content_types=['text'])
def weather(message):
    if '"Погода на сегодня"' in message.text:
        bot.send_message(message.chat.id, "Привет, сегодня:\n" + t_min + ',' + t_max)
    if '"Неважно, как дела?)"' in message.text:
        bot.send_message(message.chat.id, "У меня все хорошо, может быть все таки погоду?)")

reply_markup=markup

if __name__ == '__main__':
     bot.infinity_polling(none_stop=True)
import os
import telebot
import openai
from telebot import types
from dotenv import load_dotenv
from Parcing import settings

load_dotenv()

TOKEN = os.getenv('TOKEN')

bot = telebot.TeleBot(TOKEN)

API_KEY = settings.API_KEY
openai.api_key = API_KEY

@bot.message_handler(commands=['start'])
def start_handler(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item = types.KeyboardButton('Привет')
    markup.add(item)

    bot.send_message(message.chat.id,
                     text="""Вас приветствует ChatGPT — чат-бот с искусственным интеллектом\nЗадайте вопрос""",
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def chatgpt_bot(message: types.Message):
    user = message.text
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {'role': "user", 'content': user}
        ],
    )
    bot.send_message(chat_id=message.chat.id, text=(response['choices'][0]['message']['content']))


if __name__ == '__main__':
    print('Bot started')
    bot.polling(non_stop=True)

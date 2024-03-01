from telebot import TeleBot
from telebot.types import Message

bot = TeleBot('7005370883:AAGNibRcsHZQBV_C05XQOMyRGpGZffU8-Wk')

@bot.message_handler(commands=['start', 'help'])
def start(message: Message):
    chat_id = message.chat.id
    name = message.from_user.full_name
    bot.send_message(chat_id, f"Assalomu aleykum {name}")

@bot.message_handler(content_types=['text', 'photo', 'animation', 'video'])
def get_text(message: Message):
    chat_id = message.chat.id
    bot.copy_message(4176321143, chat_id, message.message_id)


bot.polling()
from telebot import TeleBot

token = '7775775931:AAG-Fdr5OW6z2XFcHy8kT7WOvQzObsVordo'
bot = TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Приветики-пистолетики!')


bot.infinity_polling()


import telebot

with open('Token/token.txt', 'r') as file:
    token = file.read().strip()
    file.close()

bot = telebot.TeleBot(f'{token}')

print('Bot started...')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

bot.polling(none_stop=True)
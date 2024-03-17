import telebot

with open('Token/token.txt', 'r') as file:
    token = file.read().strip()
    file.close()

bot = telebot.TeleBot(f'{token}')

print('Bot started...')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, f'Привет {message.chat.first_name}')

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    else:
        bot.send_message(message.chat.id, 'Я тебя не понимаю')

@bot.message_handler(content_types=['photo'])
def send_photo(message):
    bot.send_message(message.chat.id, 'Крутая фотка')


bot.polling(none_stop=True)
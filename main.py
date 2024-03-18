import telebot
import easyocr
import requests
import os

token = ''

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
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    download_url = f'https://api.telegram.org/file/bot{token}/{file_info.file_path}'

    download_dir = 'downloaded_photos'
    if not os.path.exists(download_dir):
        os.makedirs(download_dir)
    download_path = os.path.join(download_dir, f'{file_id}.jpg')
    response = requests.get(download_url)

    if response.status_code == 200:
        with open(download_path, 'wb') as photo:
            photo.write(response.content)
        bot.send_message(message.chat.id, f'{text_recognition(download_path)}', reply_to_message_id=message.message_id)
    else:
        bot.reply_to(message, "Ошибка при сохранении фотографии.")

def text_recognition(img):
    reader = easyocr.Reader(['ru', 'en'], gpu=False, verbose=False)
    result = reader.readtext(img)

    with open('result.txt', 'w') as file:
        for line in result:
            file.write(f'{line[1]}\n')
        file.close()

    return f"Результат распознавания: {result}"

bot.polling(none_stop=True)
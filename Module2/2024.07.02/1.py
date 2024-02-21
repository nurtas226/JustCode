import telebot

API_TOKEN = '1391778632:AAEi7fPZVqvTMm25pSpNOdSCmv6Qq9ICy0Q'

films = [
    {"title": "21", "url": "https://gidonline.com/mclksdc/21_film_url"},
    {"title": "Inception", "url": "https://gidonline.com/mclksdc/inception_film_url"},
]

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hey! To get link of movie please choose title!.")

@bot.message_handler(func=lambda message: True)
def get_film_url(message):
    film_title = message.text
    film_found = False
    for film in films:
        if film['title'].lower() == film_title.lower():
            bot.send_message(message.chat.id, f"Here is link: '{film['title']}': {film['url']}")
            film_found = True
            break
    if not film_found:
        bot.send_message(message.chat.id, f"Movie '{film_title}' is not found.")

@bot.message_handler(commands=['all_films'])
def send_all_films(message):
    bot.send_message(message.chat.id, "List of movies:")
    for film in films:
        bot.send_message(message.chat.id, f"Titles: {film['title']}")

bot.polling()
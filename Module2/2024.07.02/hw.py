import telebot
from telebot import types

API_TOKEN = ''

films = [
    {"title": "21", "genre": "Drama", "url": "https://gidonline.com/mclksdc/21_film_url"},
    {"title": "Inception", "genre": "Sci-Fi", "url": "https://gidonline.com/mclksdc/inception_film_url"},
    {"title": "Harry Potter", "genre": "Fantasy", "url": "https://gidonline.com/mclksdc/inception_film_url"},
    {"title": "1+1", "genre": "Drama", "url": "https://gidonline.com/mclksdc/inception_film_url"},
]

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['start'])
def start_command_handler(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    item1 = types.InlineKeyboardButton("Поиск по жанру", callback_data='search_by_genre')
    item2 = types.InlineKeyboardButton("Показать все фильмы", callback_data='show_all_films')
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Главное меню", reply_markup=markup)

@bot.message_handler(commands=['start'])
def start_command_handler_reply_kb(message):
    markup = types.ReplyKeyboardMarkup(row_width=2)
    item1 = types.KeyboardButton("Поиск по жанру")
    item2 = types.KeyboardButton("Показать все фильмы")
    markup.add(item1, item2)
    bot.send_message(message.chat.id, "Главное меню", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == 'show_all_films')
def show_all_films_callback_handler(call):
    films_text = "\n".join([f"{film['title']} - {film['genre']}" for film in films])
    bot.send_message(call.message.chat.id, "Список всех фильмов:\n" + films_text)

@bot.callback_query_handler(func=lambda call: call.data == 'search_by_genre')
def search_by_genre_callback_handler(call):
    markup = types.InlineKeyboardMarkup(row_width=1)
    genres = set([film['genre'] for film in films])
    for genre in genres:
        button = types.InlineKeyboardButton(genre, callback_data=f'search_genre_{genre}')
        markup.add(button)
    bot.send_message(call.message.chat.id, "Выберите жанр:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith('search_genre_'))
def search_genre_callback_handler(call):
    selected_genre = call.data.split('_')[-1]
    films_with_genre = [film for film in films if film['genre'] == selected_genre]
    films_text = "\n".join([f"{film['title']} - {film['genre']}" for film in films_with_genre])
    bot.send_message(call.message.chat.id, f"Фильмы в жанре '{selected_genre}':\n" + films_text)

bot.polling()
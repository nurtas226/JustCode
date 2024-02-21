import telebot
from telebot import types
import random

# Replace 'YOUR_API_TOKEN' with your bot's API token
API_TOKEN = '1391778632:AAEi7fPZVqvTMm25pSpNOdSCmv6Qq9ICy0Q'

# Initialize the bot
bot = telebot.TeleBot(API_TOKEN)

# Dictionary with questions and answers
questions = {
    "What is the most popular programming language?": ["Python", "Java", "C++", "JavaScript"],
    "What is the capital of France?": ["Paris", "Berlin", "London", "Madrid"],
    "Who wrote 'Crime and Punishment'?": ["Fyodor Dostoevsky", "Leo Tolstoy", "Ivan Turgenev", "Alexander Pushkin"],
    "What is the tallest mountain peak in the world?": ["Mount Everest", "K2", "Kangchenjunga", "Lhotse"],
    "Which element in the periodic table is denoted by the symbol 'O'?": ["Oxygen", "Hydrogen", "Carbon", "Nitrogen"]
}

# Dictionary to store the current question for each user
user_questions = {}

# Function to send a question to the user
def send_question(message):
    chat_id = message.chat.id
    question = random.choice(list(questions.keys()))
    user_questions[chat_id] = question

    markup = types.InlineKeyboardMarkup(row_width=2)
    options = questions[question]
    random.shuffle(options)
    for option in options:
        markup.add(types.InlineKeyboardButton(option, callback_data=option))

    bot.send_message(chat_id, question, reply_markup=markup)

# Handler for the /start command
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Hi! Let's play a quiz. I'll ask you a question, and you choose one of the options.")

# Handler for text messages (answers to questions)
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    if chat_id in user_questions:
        question = user_questions.pop(chat_id)
        answer = message.text
        correct_answer = questions[question][0]
        if answer == correct_answer:
            bot.send_message(chat_id, "Correct!")
        else:
            bot.send_message(chat_id, f"Incorrect! The correct answer is: {correct_answer}")
        send_question(message)
    else:
        bot.send_message(chat_id, "To start the game, type /start")

# Handler for the /stop command
@bot.message_handler(commands=['stop'])
def stop(message):
    chat_id = message.chat.id
    if chat_id in user_questions:
        user_questions.pop(chat_id)
        bot.send_message(chat_id, "The game is over. To start a new game, type /start")
    else:
        bot.send_message(chat_id, "The game has not started. To start the game, type /start")

# Handler for the /help command
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "To start the game, type /start. Then I will ask you a question, and you choose one of the options.")

# Handler for callback queries (option selection)
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    chat_id = call.message.chat.id
    if chat_id in user_questions:
        question = user_questions[chat_id]
        answer = call.data
        correct_answer = questions[question][0]
        if answer == correct_answer:
            bot.send_message(chat_id, "Correct!")
        else:
            bot.send_message(chat_id, f"Incorrect! The correct answer is: {correct_answer}")
        send_question(call.message)
    else:
        bot.send_message(chat_id, "To start the game, type /start")

# Start the bot
bot.polling()

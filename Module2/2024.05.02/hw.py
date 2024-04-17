import telebot
import random

API_TOKEN = ""

bot = telebot.TeleBot(token = API_TOKEN)

stickers = [
    'CAACAgIAAxkBAAELa2hlz9QTa30CAAEDeRweoC-KLq1NAfMAAqETAALfx0FJogvBoegNFCQ0BA',
    'CAACAgIAAxkBAAELa2Zlz9QHQyNQxxpdKWFAegABAfvFERQAAn0BAAJ0-FQbZwSObiEcM2s0BA',
    'CAACAgIAAxkBAAELVEJlwjoSZ18iibCnVKo3h8JzQLLuhwACpywAAp86wEpijheFyBQprTQE',
]


@bot.message_handler(commands=["start"])
def start_message(message):
    bot.send_message(message.chat.id, "Welcome! You can type /send_me_sticker to get a random sticker.")

@bot.message_handler(commands=["send_me_sticker"])
def sticker_message(message):
    try:
        random_sticker = random.choice(stickers)
        bot.send_sticker(message.chat.id, random_sticker)
    except Exception as e:
        print("An error occurred:", e)

try:
    bot.polling()
except Exception as e:
    print("An error occurred:", e)
import telebot

TOKEN = "1391778632:AAEi7fPZVqvTMm25pSpNOdSCmv6Qq9ICy0Q"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=["text"])  # обработчики сообщений: [voice, photo, video, sticker]
def message_handler_func(message):
    print(f"message: {message}")

    bot.send_message(message.chat.id, "Это текст")
    # bot.send_message(message.chat.id, message.text)


bot.polling()
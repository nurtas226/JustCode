import telebot

TOKEN = ""

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(func=lambda msg: "hello" in msg.text)
def message_handler_func(message):
    print(f"message_type: {type(message)}")
    print(f"message: {message}")

    bot.send_message(message.chat.id, "Hi:)")

    bot.reply_to(message, "Hello!")


bot.polling()
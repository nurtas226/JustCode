import telebot

TOKEN = ""

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["get_my_user_id"])
def command_handler(message):
    print(f"message: {message}")

    bot.send_message(
        chat_id=message.chat.id,
        text=f"Ваш юзер айди: {message.from_user.id}\n"
             f"Ваше имя: {message.from_user.first_name} {message.from_user.last_name}"
    )


@bot.message_handler(content_types=["text"])  # обработчики сообщений: [voice, photo, video, sticker]
def message_handler_func(message):
    print(f"message: {message}")

    bot.send_message(message.chat.id, "Это текст")


bot.polling()
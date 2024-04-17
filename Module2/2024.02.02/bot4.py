import telebot

TOKEN = ""

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(content_types=["text"])
def message_handler_func(message):
    print(f"message: {message}")

    if "hi" in message.text:
        text = "Hello"
    elif message.text == "How are you?":
        text = "All good, wbu?"
    elif message.text == "What are you doing?":
        text = "Texting you, wbu?"
    elif message.text == "How are you?":
        text = "All good, wbu?"
    elif message.text == "Whats your name?":
        text = "EchoBot, Whats yours?"
    else:
        text = "Ne ponyal:("
        # text = ""

    bot.send_message(message.chat.id, text)


bot.polling()

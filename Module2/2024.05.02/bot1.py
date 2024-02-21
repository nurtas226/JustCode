import telebot

API_TOKEN = "1391778632:AAEi7fPZVqvTMm25pSpNOdSCmv6Qq9ICy0Q"

bot = telebot.TeleBot(token = API_TOKEN)


@bot.message_handler(content_types=["photo"])
def message_handler(message):
    print(message)
    
    bot.send_message(
        chat_id = message.chat.id,
        text = "This is photo!"
        )

@bot.message_handler(content_types=["document"])
def message_handler(message):
    print(message)
    doc = message.document
    file_id = doc.file_id
    
    file_info = bot.get_file(file_id)
    file_path = file_info.file_path
    
     
    
    
    bot.send_message(
        chat_id = message.chat.id,
        text = "This is document!"
        )

@bot.message_handler(content_types=["text"])
def message_handler(message):
    print(message)
    
    bot.send_message(
        chat_id = message.chat.id,
        text = message.text
        )

bot.polling()
# bot.infinity_polling()
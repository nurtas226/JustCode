import telebot
import time

API_TOKEN = '1391778632:AAEi7fPZVqvTMm25pSpNOdSCmv6Qq9ICy0Q'

bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands=['mute'])
def mute_user(message):
    if message.reply_to_message:
        chat_id = message.chat.id
        user_id = message.reply_to_message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status
        if user_status == 'administrator' or user_status == 'creator':
            bot.reply_to(message, "Невозможно замутить администратора.")
        else:
            duration = 10
            bot.restrict_chat_member(chat_id, user_id, until_date=time.time()+duration*10)
            bot.reply_to(message, f"Пользователь {message.reply_to_message.from_user.username} замучен на {duration} минут.")
    else:
        bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите замутить.")
        
bot.polling()
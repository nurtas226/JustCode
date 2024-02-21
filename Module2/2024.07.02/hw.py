import telebot
from telebot.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = "1391778632:AAEi7fPZVqvTMm25pSpNOdSCmv6Qq9ICy0Q"

bot = telebot.TeleBot(token=API_TOKEN)

REPLY_KEYBOARD_OPTIONS = ["Алматы", "Астана", "Актобе", "Шымкент"]


@bot.message_handler(commands=["start"])
def handler_with_keyboard(
        message: Message
):

    markup = InlineKeyboardMarkup(row_width=2)

    btn1 = InlineKeyboardButton(text="A) Алматы", callback_data="a")
    btn2 = InlineKeyboardButton(text="B) Астана", callback_data="b")
    btn3 = InlineKeyboardButton(text="C) Астана", url="https://github.com/Kospanulan/python17_justcode")
    btn4 = InlineKeyboardButton(text="D) Астана", callback_data="b")

    markup.add(btn1, btn2, btn3, btn4)

    bot.send_message(
        chat_id=message.chat.id,
        text="Выберите город:",
        reply_markup=markup
    )


@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call: CallbackQuery):
    # print(type(call))
    # print(call)

    bot.answer_callback_query(callback_query_id=call.id, text="Принято!", show_alert=True)

    if call.data == "a":
        bot.send_message(
            chat_id=call.message.chat.id,
            text=f"Оо, ты с Алматы)"
        )
    else:
        bot.send_message(
            chat_id=call.message.chat.id,
            text=f"Переезжай в Алматы!"
        )


bot.polling()
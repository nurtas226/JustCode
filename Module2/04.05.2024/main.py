import telebot
from telebot import types

TOKEN = ""

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Я бот для выполнения команд sum и mul. "
                                      "Введите команду и список чисел через запятую.", 
                     reply_markup=generate_keyboard())

def generate_keyboard():
    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    sum_button = types.KeyboardButton("sum")
    mul_button = types.KeyboardButton("mul")
    keyboard.add(sum_button, mul_button)
    return keyboard

@bot.message_handler(func=lambda message: True)
def message_handler_func(message):
    if message.text.lower() in ['sum', 'mul']:
        handle_calculation_command(message)
    else:
        handle_other_commands(message)

def handle_calculation_command(message):
    command = message.text.lower()
    bot.send_message(message.chat.id, f"Отлично! Теперь введите список чисел через запятую для операции '{command}'.")
    bot.register_next_step_handler(message, process_calculation_command, command)

def process_calculation_command(message, command):
    try:
        numbers = message.text
        nums = [int(num) for num in numbers.split(",")]
        result = calculate(command, nums)
        bot.send_message(message.chat.id, result)
    except ValueError:
        bot.send_message(message.chat.id, "Неправильный формат данных")
    except Exception as e:
        bot.send_message(message.chat.id, f"Произошла ошибка: {e}")

def calculate(command, nums):
    if command == 'sum':
        return sum(nums)
    elif command == 'mul':
        result = 1
        for num in nums:
            result *= num
        return result
    else:
        return "Неправильная команда"

def handle_other_commands(message):
    bot.send_message(message.chat.id, "Неправильный формат команды")

bot.polling()
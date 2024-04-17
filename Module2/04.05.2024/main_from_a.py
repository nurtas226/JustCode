import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from aiogram.utils.markdown import hbold

TOKEN = '' # PASTE YOUR TOKEN HERE
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!")


@dp.message(Command('help'))
async def command_start_handler(message: Message):
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}, чем мы можем вам помочь?!")

# @dp.message()                                             ### Old code
# async def echo_handler(message: types.Message):
#     try:
#         await message.send_copy(chat_id=message.chat.id)
#     except TypeError:
#         await message.answer("Nice try!")

# @dp.message()                                             ### exercise1
# async def echo_handler(message: types.Message):
#     try:
#         response = message.text.upper()
#         await message.answer(response)
#     except TypeError:
#         await message.answer("Nice try!")

@dp.message()                                               ### exercise2
async def echo_handler(message: types.Message):
    
    count_words = message.text.split()
    num_words = len(count_words)
    
    if num_words > 2:
        try:
            response = message.text.upper()
            await message.answer(response)
        except TypeError:
            await message.answer("Nice try!")


async def main():
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
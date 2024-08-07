import logging
from aiogram import Bot, Dispatcher, executor, types
from checking import forwork

API_TOKEN = '7405202068:AAGUr7xHJhEG_7rNxYH_jKUQecP3N8ah4aA'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum.😉\n\nImlo tekshiruvchi to'g'riso'z botimizga xush kelibsiz")

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply("Botga istalgan so'zingizni yuboring")

@dp.message_handler()
async def check_spelling(message: types.Message):
    response = forwork(message.text)
    await message.reply(response)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

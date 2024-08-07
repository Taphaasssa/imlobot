import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ParseMode
from checking import forwork

API_TOKEN = '7405202068:AAGUr7xHJhEG_7rNxYH_jKUQecP3N8ah4aA'
ADMIN_ID = '6146446977'  # Replace with your Telegram user ID

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# In-memory storage for user messages
user_data = {}

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Assalomu alaykum.😉\n\nImlo tekshiruvchi to'g'riso'z botimizga xush kelibsiz")

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    await message.reply("Botga istalgan so'zingizni yuboring")

@dp.message_handler(commands=['users'])
async def list_users(message: types.Message):
    if str(message.from_user.id) == ADMIN_ID:
        if user_data:
            user_list = "\n".join([f"User ID: {user_id}, Username: {info['username']}" for user_id, info in user_data.items()])
            await message.reply(f"Users:\n{user_list}")
        else:
            await message.reply("No users found.")
    else:
        await message.reply("You are not authorized to use this command.")

@dp.message_handler(commands=['messages'])
async def list_user_messages(message: types.Message):
    if str(message.from_user.id) == ADMIN_ID:
        user_id = message.get_args()
        if user_id in user_data:
            messages = "\n".join(user_data[user_id]['messages'])
            await message.reply(f"Messages from user {user_id}:\n{messages}", parse_mode=ParseMode.HTML)
        else:
            await message.reply(f"No messages found for user {user_id}.")
    else:
        await message.reply("You are not authorized to use this command.")

@dp.message_handler()
async def check_spelling(message: types.Message):
    user_id = str(message.from_user.id)
    username = message.from_user.username

    # Store user messages
    if user_id not in user_data:
        user_data[user_id] = {'username': username, 'messages': []}
    user_data[user_id]['messages'].append(message.text)

    # Check spelling
    response = forwork(message.text)
    await message.reply(response)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

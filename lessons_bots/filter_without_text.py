from aiogram import Bot, Dispatcher
from aiogram.types import Message
from token_api import API_TOKEN

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
API_TOKEN: str = API_TOKEN

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


def my_start_filter(message: Message) -> bool:
    return message.text == '/start'



# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(my_start_filter)
async def process_start_command(message: Message):
    print(message.json(indent=4))
    await message.answer(text='Это команда /start')


if __name__ == '__main__':
    dp.run_polling(bot)
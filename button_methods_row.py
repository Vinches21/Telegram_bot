from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Text
from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove)
from aiogram.utils.keyboard import ReplyKeyboardBuilder

# Вместо BOT TOKEN HERE нужно вставить токен вашего бота,
# полученный у @BotFather
API_TOKEN: str = '5928240016:AAFu8zLiC8mstjLTzSlwd4i0vbeNRApFYNA'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()

#Инициализируем объект билдера
kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()


# Создаем список с кнопками (например, 10 кнопок)
buttons: list[KeyboardButton] = [
    KeyboardButton(text=f'Кнопка {i}') for i in range(1, 11)]
print(*buttons)

# Методами билдера добавляем в него кнопки (возьмем для примера метод row())
kb_builder.row(*buttons, width=4)


#Методом as_markup() передаем клавиатуру как аргумент туда, где она требуется
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Количество кнопок',
                         reply_markup=kb_builder.as_markup(resize_keyboard=True))

if __name__ == '__main__':
    dp.run_polling(bot)



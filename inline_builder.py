import asyncio
import logging
from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config

from aiogram.filters import CommandStart, Text
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder



# Загружаем конфиг в переменную config
config: Config = load_config()

# Инициализируем бот и диспетчер
bot: Bot = Bot(token=config.tg_bot.token)
dp: Dispatcher = Dispatcher()

kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()

# Создаем объекты инлайн-кнопок
button_1: InlineKeyboardButton = InlineKeyboardButton(
    text='Человек',
    callback_data='big_button_1_pressed')

button_2: InlineKeyboardButton = InlineKeyboardButton(
    text='Кот',
    callback_data='big_button_2_pressed')

button_3: InlineKeyboardButton = InlineKeyboardButton(
    text='Морж',
    callback_data='big_button_2_pressed')

button_4: InlineKeyboardButton = InlineKeyboardButton(
    text='Петух',
    callback_data='big_button_2_pressed')

button_5: InlineKeyboardButton = InlineKeyboardButton(
    text='Дельфин',
    callback_data='big_button_2_pressed')

button_6: InlineKeyboardButton = InlineKeyboardButton(
    text='Слон',
    callback_data='big_button_2_pressed')

button_7: InlineKeyboardButton = InlineKeyboardButton(
    text='Динозавр',
    callback_data='big_button_2_pressed')

button_8: InlineKeyboardButton = InlineKeyboardButton(
    text='Робот',
    callback_data='big_button_2_pressed')

# kb_builder.row(button_1, button_2, button_3, width=2)
kb_builder.row(button_1, button_2, button_3, button_4, button_5, button_6, button_7, width=2)
kb_builder.adjust(2, 1, 3)

kb_2 = kb_builder.copy()

kb_2.row(button_8)



@dp.message(CommandStart())
async def process_start_command(message:Message):
    await message.answer(text="Это три инлайн кнопки с методом //start",
                         reply_markup=kb_2.as_markup(resize_keyboard=True))


if __name__ == '__main__':
    dp.run_polling(bot)


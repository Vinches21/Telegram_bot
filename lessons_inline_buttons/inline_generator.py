import asyncio
import logging
from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config

from aiogram.filters import CommandStart, Text
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from keyboards.inline_button_generator import create_inline_kb
from keyboards.keyboards import game_kb

# Загружаем конфиг в переменную config
config: Config = load_config()

# Инициализируем бот и диспетчер
bot: Bot = Bot(token=config.tg_bot.token)
dp: Dispatcher = Dispatcher()

@dp.message(CommandStart())
async def process_start_command(message: Message):
    #Позиционные аргументы
    # keyboard = create_inline_kb(2, 'but_1', 'but_3', 'but_7')
    #Именнованные аргументы
    keyboard = create_inline_kb(2, btn_tel='Телефон',
                                btn_email='email',
                                btn_website='Web-сайт',
                                btn_vk='VK',
                                btn_tgbot='Наш телеграм-бот')

    await message.answer(text='Вот такая получается клавиатура',
                         reply_markup=keyboard)


if __name__ == '__main__':
    dp.run_polling(bot)


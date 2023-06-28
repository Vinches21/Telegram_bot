from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon_ru import LEXICON_RU
from keyboards.keyboards import game_kb, yes_no_kb
router: Router = Router()


# Хэндлер для сообщений, которые не попали в другие хэндлеры
@router.message()
async def send_answer(message: Message):
    await message.answer(text=LEXICON_RU['other_answer'])
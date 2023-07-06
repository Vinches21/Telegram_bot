from aiogram import Bot, Dispatcher
from aiogram.types import (CallbackQuery, InlineKeyboardButton,
                           InlineKeyboardMarkup, InputMediaAudio,
                           InputMediaDocument, InputMediaPhoto,
                           InputMediaVideo, Message)
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.filters import CommandStart, Text
from aiogram.exceptions import TelegramBadRequest

from config_data.config import load_config

config = load_config()

bot: Bot = Bot(token=config.tg_bot.token)
dp: Dispatcher = Dispatcher()


LEXICON: dict[str, str] = {
    'audio': '🎶 Аудио',
    'text': '📃 Текст',
    'photo': '🖼 Фото',
    'video': '🎬 Видео',
    'document': '📑 Документ',
    'voice': '📢 Голосовое сообщение',
    'text_1': 'Это обыкновенное текстовое сообщение, его можно легко отредактировать другим текстовым сообщением, но нельзя отредактировать сообщением с медиа.',
    'text_2': 'Это тоже обыкновенное текстовое сообщение, которое можно заменить на другое текстовое сообщение через редактирование.',
    'photo_id1': 'AgACAgIAAxkBAAIFNmSmpZvyEmAMz6RjXeX3dpxxN2hmAALFyTEbDLcxScgK8F5GxZlfAQADAgADcwADLwQ',
    'photo_id2': 'AgACAgIAAxkBAAIFOGSmpikZzDCJajP55Gw5pKyILnteAALOyTEbDLcxScxL2FjEvGnUAQADAgADcwADLwQ',
    'voice_id1': 'AwACAgIAAxkBAAIFQGSmpt78WbE1TINwJQrETgX7Cpx0AALqMAACDLcxSaCAAfrHNzwTLwQ',
    'voice_id2': 'AwACAgIAAxkBAAIFQmSmpvULYWKFMuS1S-8coZtFdH_qAALrMAACDLcxSdFcnfaI7P7oLwQ',
    'audio_id1': 'CQACAgIAAxkBAAIFRGSmpyLyAXdnjn13yGhyo4pPZO_wAALsMAACDLcxSdMVbNjZ7etoLwQ',
    'audio_id2': 'CQACAgIAAxkBAAIFRmSmp0FAa7Uk_chilFJss74-Ef_gAALyMAACDLcxSUVZiBlWTV0TLwQ',
    'document_id1': 'BQACAgIAAxkBAAIFOmSmpmy2qKi9s2elTaZMojYqF-pNAALlMAACDLcxSa2V9-XH1Q_GLwQ',
    'document_id2': 'BQACAgIAAxkBAAIFPGSmppQdYJuBgzy6ufm1JEeLj3IWAALmMAACDLcxSaldZ-0wZIYYLwQ',
    'video_id1': 'BAACAgIAAxkBAAIFSmSmp6-qnG5GmIfyzzF1WsNMc6gsAAL4MAACDLcxSTk1wEo92elKLwQ',
    'video_id2': 'BAACAgIAAxkBAAIFTGSmp8UZQhj-vUpY1ww5_66fsnjxAAL5MAACDLcxSeJj5MsAASPyOC8E',
    }


# Функция для генерации клавиатур с инлайн-кнопками
def get_markup(width: int, *args, **kwargs) -> InlineKeyboardMarkup:
    # Инициализируем билдер
    kb_builder: InlineKeyboardBuilder = InlineKeyboardBuilder()
    # Инициализируем список для кнопок
    buttons: list[InlineKeyboardButton] = []
    # Заполняем список кнопками из аргументов args и kwargs
    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=LEXICON[button] if button in LEXICON else button,
                callback_data=button))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button))
    # Распаковываем список с кнопками в билдер методом row c параметром width
    kb_builder.row(*buttons, width=width)
    # Возвращаем объект инлайн-клавиатуры
    return kb_builder.as_markup()


# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(CommandStart())
async def process_start_command(message: Message):
    markup = get_markup(2, 'document')
    await message.answer_document(
                        document=LEXICON['document_id1'],
                        caption='Это документ 1',
                        reply_markup=markup)


# Этот хэндлер будет срабатывать на нажатие инлайн-кнопки
@dp.callback_query(Text(text=['text',
                              'audio',
                              'video',
                              'document',
                              'photo',
                              'voice']))
async def process_button_press(callback: CallbackQuery, bot: Bot):
    markup = get_markup(2, 'document')
    try:
        await bot.edit_message_media(
                        chat_id=callback.message.chat.id,
                        message_id=callback.message.message_id,
                        media=InputMediaDocument(
                                media=LEXICON['document_id2'],
                                caption='Это документ 2'),
                        reply_markup=markup)
    except TelegramBadRequest:
        await bot.edit_message_media(
                        chat_id=callback.message.chat.id,
                        message_id=callback.message.message_id,
                        media=InputMediaDocument(
                                media=LEXICON['document_id1'],
                                caption='Это документ 1'),
                        reply_markup=markup)


# Этот хэндлер будет срабатывать на все остальные сообщения
@dp.message()
async def send_echo(message: Message):
    print(message)
    await message.answer(
            text='Не понимаю')


if __name__ == '__main__':
    dp.run_polling(bot)
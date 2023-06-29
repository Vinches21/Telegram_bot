from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Text
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType, Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types.web_app_info import WebAppInfo


API_TOKEN: str = '5928240016:AAFu8zLiC8mstjLTzSlwd4i0vbeNRApFYNA'

# Создаем объекты бота и диспетчера
bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


# Инициализируем билдер
kb_builder: ReplyKeyboardBuilder = ReplyKeyboardBuilder()

# Создаем кнопки
contact_btn: KeyboardButton = KeyboardButton(
                                text='Отправить телефон',
                                request_contact=True)
geo_btn: KeyboardButton = KeyboardButton(
                                text='Отправить геолокацию',
                                request_location=True)
poll_btn: KeyboardButton = KeyboardButton(
                                text='Создать опрос/викторину',
                                request_poll=KeyboardButtonPollType())

web_app_btn: KeyboardButton = KeyboardButton(
                                text='Start Web App',
                                web_app=WebAppInfo(url="https://lookdecor.ru/"))

# Добавляем кнопки в билдер
kb_builder.row(contact_btn, geo_btn, poll_btn, web_app_btn, width=1)

# Создаем объект клавиатуры
keyboard: ReplyKeyboardMarkup = kb_builder.as_markup(
                                    resize_keyboard=True,
                                    one_time_keyboard=True)




# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text='Выбери вариант',
                         reply_markup=keyboard)

@dp.message(F.contact)
async def process_answer_mobile(message: Message):
    await message.answer(text="Вот же дурак!!!")

# Этот хэндлер будет срабатывать на команду "/web_app"


if __name__ == '__main__':
    dp.run_polling(bot)


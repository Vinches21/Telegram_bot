from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

from token_api import API_TOKEN


# Создаем объекты бота и диспетчера

bot: Bot = Bot(token=API_TOKEN)
dp: Dispatcher = Dispatcher()


# Этот хэндлер будет срабатывать на команду "/start"
async def process_start_command(message: Message):
    await message.answer('Привет!\nМеня зовут Эхо-бот!\nНапиши мне что-нибудь')


# Этот хэндлер будет срабатывать на команду "/help"
async def process_help_command(message: Message):
    await message.answer('Напиши мне что-нибудь и в ответ '
                         'я пришлю тебе твое сообщение')


# Этот хэндлер будет срабатывать на отправку боту фото
async def send_photo_echo(message: Message):
    print(message.json(indent=4))
    await message.reply_photo(message.photo[0].file_id)


#Этот хендлер будет срабатывать на отправку боту видео

async def send_video_echo(message: Message):
    print(message.json(indent=4))
    await message.reply_video(message.video.file_id)

#Этот хэндлер будет срабатывать на отправку боту голосового сообщения
async def send_golos(message: Message):
    print(message.json(indent=4))
    await message.reply_voice(message.voice.file_id)


#Этот хендлер будет срабатывать на отправку боту стикера
async def send_sticker(message: Message):
    print(message.json(indent=4))
    await message.reply_sticker(message.sticker.file_id)

# Этот хэндлер будет срабатывать на отправку gif
async def send_gif(message:Message):
    print(message.json(indent=4))
    await message.reply_animation(message.animation.file_id)

#Этот хэндлер будет срабатывать на отправку document

async def send_document(message: Message):
    print(message.json(indent=4, exclude_none=True))
    await message.reply_document(message.document.file_id)

# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
async def send_echo(message: Message):
    await message.reply(text=message.text)




# Регистрируем хэндлеры
dp.message.register(process_start_command, Command(commands=["start"]))
dp.message.register(process_help_command, Command(commands=['help']))
dp.message.register(send_photo_echo, F.photo)
dp.message.register(send_video_echo, F.video)
dp.message.register(send_golos, F.voice)
dp.message.register(send_sticker, F.sticker)
dp.message.register(send_gif, F.animation)
dp.message.register(send_document, F.document)
dp.message.register(send_echo)

if __name__ == '__main__':
    dp.run_polling(bot)
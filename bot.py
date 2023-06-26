import asyncio

from aiogram import Bot, Dispatcher
from config_data.config import Config, load_config
from create_dp import dp


# Функция конфигурирования и запуска бота
async def main(dp: Dispatcher):

    # Загружаем конфиг в переменную config
    config: Config = load_config()
    # Инициализируем бот
    bot: Bot = Bot(token=config.tg_bot.token)

    # Пропускаем накопившиеся апдейты и запускаем polling
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main(dp))
import logging
from aiogram import Bot, Dispatcher, types
import asyncio


BOT_TOKEN = "ВСТАВИТЬ ТОКЕН"


HORROR_IMAGE_PATH = "image/horror.png"
DETECTIVE_IMAGE_PATH = "image/detective.png"
COMEDY_IMAGE_PATH = "image/comedy.png"
ACTION_IMAGE_PATH = "image/action.png"
ADVENTURE_IMAGE_PATH = "image/adventure.png"
ANIMATION_IMAGE_PATH = "image/animation.png"
DRAMA_IMAGE_PATH = "image/drama.png"
FANTASY_IMAGE_PATH = "image/fantasy.png"
ROMANTIC_IMAGE_PATH = "image/romantic.png"
SCIFI_IMAGE_PATH = "image/SCI-FI.png"
THRILLER_IMAGE_PATH = "image/thriller.png"
WESTERN_IMAGE_PATH = "image/western.png"



logging.basicConfig(level=logging.INFO)


bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

@dp.message_handler(lambda message: message.text.lower() == "ужасы")
async def send_horror_image(message: types.Message):
    """Обработчик для жанра 'Ужасы'."""
    logging.info(f"Received message: {message.text} from {message.from_user.username}")
    try:
        with open(HORROR_IMAGE_PATH, 'rb') as photo:
            await message.reply_photo(photo=photo, caption="Ваше описание похоже на жанр ужасы")
    except FileNotFoundError:
        await message.answer("К сожалению, не удалось определить жанр вашего фильма")

@dp.message_handler(lambda message: message.text.lower() == "детектив")
async def send_detective_image(message: types.Message):
    """Обработчик для жанра 'Детектив'."""
    logging.info(f"Received message: {message.text} from {message.from_user.username}")
    try:
        with open(DETECTIVE_IMAGE_PATH, 'rb') as photo:
            await message.reply_photo(photo=photo, caption="Ваше описание похоже на жанр детектив")
    except FileNotFoundError:
        await message.answer("К сожалению, не удалось определить жанр вашего фильма")

@dp.message_handler(lambda message: message.text.lower() == "комедия")
async def send_comedy_image(message: types.Message):
    """Обработчик для жанра 'Комедия'."""
    logging.info(f"Received message: {message.text} from {message.from_user.username}")
    try:
        with open(COMEDY_IMAGE_PATH, 'rb') as photo:
            await message.reply_photo(photo=photo, caption="Ваше описание похоже на жанр комедия")
    except FileNotFoundError:
        await message.answer("К сожалению, не удалось определить жанр вашего фильма")

@dp.message_handler(lambda message: message.text.lower() == "боевик")
async def send_action_image(message: types.Message):
    """Обработчик для жанра 'Боевик'."""
    logging.info(f"Received message: {message.text} from {message.from_user.username}")
    try:
        with open(ACTION_IMAGE_PATH, 'rb') as photo:
            await message.reply_photo(photo=photo, caption="Ваше описание похоже на жанр боевик")
    except FileNotFoundError:
        await message.answer("К сожалению, не удалось определить жанр вашего фильма")

@dp.message_handler(lambda message: message.text.lower() == "приключения")
async def send_adventure_image(message: types.Message):
    """Обработчик для жанра 'Приключения'."""
    logging.info(f"Received message: {message.text} from {message.from_user.username}")
    try:
        with open(ADVENTURE_IMAGE_PATH, 'rb') as photo:
            await message.reply_photo(photo=photo, caption="Ваше описание похоже на жанр приключения")
    except FileNotFoundError:
        await message.answer("К сожалению, не удалось определить жанр вашего фильма")

@dp.message_handler(lambda message: message.text.lower() == "анимация")
async def send_animation_image(message: types.Message):
    """Обработчик для жанра 'Анимация'."""
    logging.info(f"Received message: {message.text} from {message.from_user.username}")
    try:
        with open(ANIMATION_IMAGE_PATH, 'rb') as photo:
            await message.reply_photo(photo=photo, caption="Ваше описание похоже на жанр анимация")
    except FileNotFoundError:
        await message.answer("К сожалению, не удалось определить жанр вашего фильма")

@dp.message_handler(lambda message: message.text.lower() == "драма")
async def send_drama_image(message: types.Message):
    """Обработчик для жанра 'Драма'."""
    logging.info(f"Received message: {message.text} from {message.from_user.username}")
    try:
        with open(DRAMA_IMAGE_PATH, 'rb') as photo:
            await message.reply_photo(photo=photo, caption="Ваше описание похоже на жанр драма")
    except FileNotFoundError:
        await message.answer("К сожалению, не удалось определить жанр вашего фильма")

@dp.message_handler(lambda message: message.text.lower() == "фэнтези")
async def send_fantasy_image(message: types.Message):
    """Обработчик для жанра 'Фэнтези'."""
    logging.info(f"Received message: {message.text} from {message.from_user.username}")
    try:
        with open(FANTASY_IMAGE_PATH, 'rb') as photo:
            await message.reply_photo(photo=photo, caption="Ваше описание похоже на жанр фэнтези")
    except FileNotFoundError:
        await message.answer("К сожалению, не удалось определить жанр вашего фильма")

@dp.message_handler(lambda message: message.text.lower() == "романтика")
async def send_romantic_image(message: types.Message):
    """Обработчик для жанра 'Романтика'."""
    logging.info(f"Received message: {message.text} from {message.from_user.username}")
    try:
        with open(ROMANTIC_IMAGE_PATH, 'rb') as photo:
            await message.reply_photo(photo=photo, caption="Ваше описание похоже на жанр романтика")
    except FileNotFoundError:
        await message.answer("К сожалению, не удалось определить жанр вашего фильма")

@dp.message_handler(lambda message: message.text.lower() == "научная фантастика")
async def send_scifi_image(message: types.Message):
    """Обработчик для жанра 'Научная фантастика'."""
    logging.info(f"Received message: {message.text} from {message.from_user.username}")
    try:
        with open(SCIFI_IMAGE_PATH, 'rb') as photo:
            await message.reply_photo(photo=photo, caption="Ваше описание похоже на жанр научная фантастика")
    except FileNotFoundError:
        await message.answer("К сожалению, не удалось определить жанр вашего фильма")

@dp.message_handler(lambda message: message.text.lower() == "триллер")
async def send_thriller_image(message: types.Message):
    """Обработчик для жанра 'Триллер'."""
    logging.info(f"Received message: {message.text} from {message.from_user.username}")
    try:
        with open(THRILLER_IMAGE_PATH, 'rb') as photo:
            await message.reply_photo(photo=photo, caption="Ваше описание похоже на жанр триллер")
    except FileNotFoundError:
        await message.answer("К сожалению, не удалось определить жанр вашего фильма")

@dp.message_handler(lambda message: message.text.lower() == "вестерн")
async def send_western_image(message: types.Message):
    """Обработчик для жанра 'Вестерн'."""
    logging.info(f"Received message: {message.text} from {message.from_user.username}")
    try:
        with open(WESTERN_IMAGE_PATH, 'rb') as photo:
            await message.reply_photo(photo=photo, caption="Ваше описание похоже на жанр вестерн")
    except FileNotFoundError:
        await message.answer("К сожалению, не удалось определить жанр вашего фильма")

async def main():
    """Основная функция запуска бота."""
    try:
        print("Бот запущен.")
        await dp.start_polling(bot)
    except KeyboardInterrupt:
        print("Бот завершил работу.")
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
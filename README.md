# genry_film_bot

# Документация для Telegram-бота

## Описание проекта

Telegram-бот создан для определения жанра фильма по его описанию. Пользователь отправляет боту текст, содержащий описание фильма, а бот анализирует текст и возвращает предполагаемый жанр с соответствующим изображением.

## Технологии и зависимости

- **Язык программирования:** Python
- **Используемые библиотеки:**
  - aiogram: для создания Telegram-бота и обработки сообщений.
  - logging: для логирования событий.
  - asyncio: для асинхронного запуска бота.

## Установка

1. Клонируйте репозиторий с ботом.
2. Установите необходимые зависимости:
   ```bash
   pip install aiogram
   ```
3. Убедитесь, что у вас установлен Python версии 3.7 или выше.
4. Скачайте изображения жанров и сохраните их в папке `image/` рядом с файлом скрипта. Имена файлов должны совпадать с указанными в коде (например, `horror.png`, `detective.png`, и т.д.).

## Конфигурация

1. Получите токен для вашего бота в BotFather.
2. В коде замените строку `BOT_TOKEN` на ваш токен:
   ```python
   BOT_TOKEN = "ВАШ_ТОКЕН_БОТА"
   ```
3. Убедитесь, что пути к изображениям соответствуют вашему файловому хранилищу.

## Функционал

### Поддерживаемые жанры:

- Ужасы
- Детектив
- Комедия
- Боевик
- Приключения
- Анимация
- Драма
- Фэнтези
- Романтика
- Научная фантастика
- Триллер
- Вестерн

### Описание работы:

1. Пользователь отправляет описание фильма, содержащее ключевые элементы сюжета, а бот анализирует текст и определяет предполагаемый жанр.
2. Бот отвечает изображением, связанным с этим жанром, и текстовым сообщением, подтверждающим выбор.
3. Если жанр бот не определил, он об этом пишет.

### Обработчики сообщений:

Для каждого жанра реализован отдельный обработчик. Например, для жанра "Ужасы":

```python
@dp.message_handler(lambda message: message.text.lower() == "ужасы")
async def send_horror_image(message: types.Message):
    logging.info(f"Received message: {message.text} from {message.from_user.username}")
    try:
        with open(HORROR_IMAGE_PATH, 'rb') as photo:
            await message.reply_photo(photo=photo, caption="Ваше описание похоже на жанр ужасы")
    except FileNotFoundError:
        await message.answer("К сожалению, не удалось определить жанр вашего фильма")
```

### Логирование:

Все входящие сообщения записываются в лог с указанием текста сообщения и имени пользователя:

```python
logging.info(f"Received message: {message.text} from {message.from_user.username}")
```

## Запуск бота

1. Запустите скрипт:
   ```bash
   python bot.py
   ```
2. Если бот успешно запущен, в консоли отобразится сообщение:
   ```
   Бот запущен.
   ```

## Обработка исключений

1. Если файл изображения не найден, бот уведомит пользователя о невозможности обработки запроса.
2. Для завершения работы бота используйте комбинацию клавиш `Ctrl+C`. При этом бот завершит свою сессию корректно.

## Расширение функционала

- Добавление новых жанров возможно через добавление соответствующего обработчика в код и изображения в папку `image/`.
- Интеграция нейросети для анализа описания и определения жанра на основе текста.


import telegram
from telegram.ext import Updater, CommandHandler

# здесь нужно вставить ваш токен Telegram и токен для API моего сервиса
telegram_token = 'YOUR_TELEGRAM_TOKEN'
openai_token = 'YOUR_OPENAI_TOKEN'

# создаем экземпляр бота и подключаемся к Telegram API
bot = telegram.Bot(token=telegram_token)
updater = Updater(token=telegram_token, use_context=True)

# функция-обработчик команды /hello
def hello(update, context):
    # получаем сообщение от пользователя
    message = update.message.text

    # используем API OpenAI для генерации ответа на сообщение пользователя
    response = openai_api(message)

    # отправляем ответ пользователю
    update.message.reply_text(response)

# функция для обращения к API OpenAI
def openai_api(message):
    # создаем экземпляр API и делаем запрос на генерацию ответа
    api = openai.ApiClient(openai_token)
    response = api.completions.create(
        engine="davinci",
        prompt=message,
        max_tokens=60
    )

    # извлекаем сгенерированный ответ из ответа API
    text = response.choices[0].text.strip()
    return text

# создаем обработчик команды /hello
hello_handler = CommandHandler('hello', hello)

# регистрируем обработчик в системе обработки событий бота
updater.dispatcher.add_handler(hello_handler)

# запускаем бота
updater.start_polling()
updater.idle()

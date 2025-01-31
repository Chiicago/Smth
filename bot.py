from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import config

# Функция для обработки команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Я ваш бот. Напишите мне что-нибудь, и я отвечу!")

# Функция для обработки текстовых сообщений
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.reply_text(f"Вы написали: {user_message}")

def main():
    # Укажите ваш токен Telegram API
    TOKEN = config.TOKEN

    # Создание приложения
    application = Application.builder().token(TOKEN).build()

    # Добавление обработчиков
    application.add_handler(CommandHandler("start", start))  # Обработка команды /start
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))  # Обработка текстовых сообщений

    # Запуск бота
    application.run_polling()

if __name__ == "__main__":
    main()
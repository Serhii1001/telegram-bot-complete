import logging
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import config

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

async def reply_all(update: Update, context: ContextTypes.DEFAULT_TYPE):
    phrase = random.choice(config.PHRASES)
    await update.message.reply_text(phrase)

async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE):
    logger.error(msg="Exception while handling an update:", exc_info=context.error)

def main():
    app = ApplicationBuilder().token(config.BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, reply_all))
    app.add_error_handler(error_handler)
    app.run_polling()

if __name__ == '__main__':
    main()

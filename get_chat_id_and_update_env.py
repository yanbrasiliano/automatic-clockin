from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
from dotenv import load_dotenv, set_key

print("Loading environment variables...")
load_dotenv()

# Get the token from .env file
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
ENV_FILE_PATH = '.env'

print(f"TELEGRAM_TOKEN: {TELEGRAM_TOKEN}")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("Received /start command")
    chat_id = update.message.chat_id
    await update.message.reply_text(f'Your chat ID is: {chat_id}')
    
    # Update the .env file with the new CHAT_ID
    set_key(ENV_FILE_PATH, 'CHAT_ID', str(chat_id))
    await update.message.reply_text('CHAT_ID has been updated in the .env file.')
    print(f"CHAT_ID updated in .env file: {chat_id}")

def main():
    print("Creating application...")
    # Create the Application and pass it your bot's token.
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    
    print("Adding command handler...")
    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))

    print("Starting the bot...")
    # Start the Bot
    application.run_polling()

    print("Bot is running...")

if __name__ == '__main__':
    main()

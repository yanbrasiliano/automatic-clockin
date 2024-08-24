from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os
from dotenv import load_dotenv
import subprocess
import asyncio

load_dotenv()

# Get credentials and paths from .env file
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')
SCREENSHOT_PATH = os.getenv('SCREENSHOT_PATH')
SCRIPT_PATH = os.getenv('SCRIPT_PATH')


async def send_message(application, chat_id: str, message: str):
    await application.bot.send_message(chat_id=chat_id, text=message)
    print(f"Sent message to {chat_id}: {message}")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print("Received /start command")
    await send_message(context.application, update.effective_chat.id, 'Do you want to register the point? Reply "Yes" to confirm or "No" to take a screenshot of the current page.')


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    print(f"Received message: {text}")
    if text.lower() in ["yes", "y"]:
        print("Processing 'Yes' response")
        # Call the point registration script
        result = subprocess.run(
            ['python3', SCRIPT_PATH], capture_output=True, text=True)
        if result.returncode == 0:
            await update.message.reply_text('Point registered successfully!')
        else:
            await update.message.reply_text(f'Error registering point: {result.stderr}')

        # Send a screenshot after registering the point
        screenshot_file = os.path.join(
            SCREENSHOT_PATH, 'screenshot_after_register.png')
        print(f"Looking for screenshot: {screenshot_file}")
        if os.path.exists(screenshot_file):
            await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(screenshot_file, 'rb'))
            print(
                f"Sent screenshot after register to {update.effective_chat.id}")
        else:
            await update.message.reply_text('Screenshot not found.')

    elif text.lower() in ["no", "n"]:
        print("Processing 'No' response")
        # Just take a screenshot of the current page after login
        screenshot_file = os.path.join(
            SCREENSHOT_PATH, 'screenshot_after_login.png')
        print(f"Looking for screenshot: {screenshot_file}")

        # Take a screenshot (assuming your script can handle taking a screenshot without performing other actions)
        result = subprocess.run(
            ['python3', SCRIPT_PATH, '--screenshot'], capture_output=True, text=True)

        if result.returncode == 0:
            await update.message.reply_text('Current page screenshot taken.')
        else:
            await update.message.reply_text(f'Error taking screenshot: {result.stderr}')

        if os.path.exists(screenshot_file):
            await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open(screenshot_file, 'rb'))
            print(
                f"Sent current page screenshot to {update.effective_chat.id}")
        else:
            await update.message.reply_text('Screenshot not found.')

    await context.application.bot.send_message(chat_id=update.effective_chat.id, text="Operation completed. Exiting now.")
    print("Operation completed. Exiting now.")
    os._exit(0)


async def wait_for_response(application, chat_id):
    try:
        await asyncio.wait_for(application.updater.start_polling(), timeout=15)
    except asyncio.TimeoutError:
        await send_message(application, chat_id, "No response received. Stopping execution.")
        print("No response received. Stopping execution.")
        os._exit(0)


async def main():
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND, handle_message))

    await application.initialize()
    await application.start()
    await send_message(application, CHAT_ID, 'Do you want to register the point? Reply "Yes" to confirm or "No" to take a screenshot of the current page.')

    # Wait for response with a timeout
    await wait_for_response(application, CHAT_ID)
    print("Bot is running...")

    # Keep the bot running
    while True:
        await asyncio.sleep(100)

if __name__ == '__main__':
    asyncio.run(main())

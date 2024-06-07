
# Automated Login and Point Registration

This project automates the login process and point registration for an intranet system using Selenium.

## Prerequisites

- Python 3.x
- Google Chrome
- Chromedriver

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/automatic-clockin.git
    cd automatic-clockin
    ```
2. Create a virtual environment:
    ```sh
    python3 -m venv myenv
    source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
    ```
3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Create a `.env` based on `.env.example` file in the root directory and add your credentials and URL:
    ```dotenv
    LOGIN=your_login
    PASSWORD=your_password
    URL=https://your.url.com
    SCREENSHOT_PATH=/path/to/your/screenshot/directory
    ```

## Integration with Telegram

This project can also send a confirmation message to your Telegram bot before executing the point registration script. Follow these steps to set it up:

### 1. Create a Telegram Bot

- Open Telegram and search for `BotFather`.
- Start a chat with `BotFather` and use the command `/newbot` to create a new bot.
- Follow the instructions to set up your bot and get the bot token.

### 2. Get the Chat ID

1. Run the script to get the `chat_id`:
    ```sh
    python get_chat_id_and_update_env.py
    ```
2. Open a chat with your bot on Telegram and send `/start`. The bot will reply with your `chat_id` and update the `.env` file automatically.

### 3. Configure the `.env` file

Ensure your `.env` file contains the following variables:
    ```dotenv
    TELEGRAM_TOKEN=your_telegram_bot_token
    CHAT_ID=your_obtained_chat_id_here
    LOGIN=your_login_value
    PASSWORD=your_password_value
    URL=your_url_here
    SCREENSHOT_PATH=/path/to/screenshot/directory
    SCRIPT_PATH=/home/hiyan/Development/personal/automatic-clockin/index.py
    ```

### 4. Sending Messages and Handling Responses

Run the script to send a message and handle responses:
    ```sh
    python send_telegram_message.py
    ```

### 5. Schedule the Script

You can schedule the script to run at specific times using cron jobs on Unix systems or Task Scheduler on Windows.

For example, to run the script every weekday at specific times, add the following lines to your crontab:
    ```sh
    50 7 * * 1-5 python3 /path/to/send_telegram_message.py
    00 12 * * 1-5 python3 /path/to/send_telegram_message.py
    30 13 * * 1-5 python3 /path/to/send_telegram_message.py
    05 18 * * 1-5 python3 /path/to/send_telegram_message.py
    ```

## Usage

Run the point registration script manually:
```sh
python index.py
```

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Testing the Integration Manually

1. **Obtain the `chat_id`**:
   - Execute `get_chat_id_and_update_env.py`:
     ```sh
     python get_chat_id_and_update_env.py
     ```
   - Open a chat with your bot on Telegram and send `/start`. The bot will reply with your `chat_id` and update the `.env` file.

2. **Test the Telegram integration**:
   - Run `send_telegram_message.py`:
     ```sh
     python send_telegram_message.py
     ```
   - Respond to the message on Telegram to see if the script behaves as expected.

3. **Run the point registration script**:
   - Execute `index.py`:
     ```sh
     python index.py
     ```

This ensures you can set up and test the integration with Telegram before automating the process using cron jobs.
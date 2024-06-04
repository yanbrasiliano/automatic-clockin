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
    python -m venv myenv
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

## Usage

Run the script:
```sh
python index.py
```

## Schedule the script

You can schedule the script to run at a specific time using cron jobs on Unix systems or Task Scheduler on Windows.

For example, to run the script every day at 8:00 AM, add the following line to your crontab:
```sh
0 8 * * * /path/to/python /path/to/automatic-clockin/index.py
```

## License

Distributed under the MIT License. See `LICENSE` for more information.
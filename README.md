# Quiz Telegram Bot

This is a simple Telegram bot that lets users participate in a quiz game. The bot asks multiple-choice questions, tracks scores, and allows users to restart the quiz.

You can try the bot here: [Quiz Telegram Bot](https://t.me/quizz_do_bot)

## Features

- **Start the quiz**: Use the `/start` command to begin the quiz.
- **Answer questions**: Multiple-choice questions with options 1-4.
- **Score tracking**: Points are awarded for correct answers, displayed after each question.
- **Restart**: Users can restart the quiz once all questions are answered.

## Requirements

- Python 3.7 or higher
- Telegram API token
- Telegram Bot username

## Installation

1. Clone the repository or download the script.
2. Install required libraries:

   ```bash
   pip install python-telegram-bot
   ```

3. Replace the `TOKEN` and `BOT_USERNAME` in the script with your bot's credentials.
4. Run the bot:

   ```bash
   python main.py
   ```

5. Start the bot on Telegram by searching for the bot's username or using the link provided by BotFather.

## How it Works

- **/start Command**: Greets the user and provides instructions.
- **/quiz Command**: Starts the quiz with random questions and answer options.
- **Answering Questions**: Users select their answer by typing the corresponding number. The bot checks the answer and awards points.
- **Completion**: Once all questions are answered, users are notified of their score and can restart the quiz.

## Hosting

The bot can be hosted on platforms like [Render](https://render.com/) or [PythonAnywhere](https://www.pythonanywhere.com/) for 24/7 access.

## File Structure

- `main.py`: The script that runs the bot and handles the quiz logic.

## License

This project is open-source and available under the [MIT License](LICENSE).

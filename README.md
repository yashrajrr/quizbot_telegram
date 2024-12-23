# quizbot_telegram
Here's the updated README with the information included so that users can directly try out the bot:

---

# Quiz Telegram Bot

This is a simple Telegram bot that allows users to participate in a quiz game. The bot asks multiple-choice questions and awards points for correct answers. Users can start the quiz, answer questions, and track their score.

You can try the bot out here: [Quiz Telegram Bot](https://t.me/quizz_do_bot)

## Features

- **Start the quiz**: Users can start the quiz with the `/start` command.
- **Answer questions**: The bot sends multiple-choice questions, and users can respond by choosing an option (1-4).
- **Score tracking**: Points are awarded for correct answers and displayed after each question.
- **Quiz completion**: Once all questions are answered, users can restart the quiz.

## Requirements

- Python 3.7 or higher
- Telegram API token (replace `TOKEN` with your own)
- Telegram Bot username (replace `BOT_USERNAME` with your own bot's username)

## Installation

1. Clone the repository or download the script to your local machine.
2. Install the required libraries using pip:

   ```bash
   pip install python-telegram-bot
   ```

3. Replace the `TOKEN` and `BOT_USERNAME` variables with your bot's actual credentials.

4. Run the bot script:

   ```bash
   python quiz_bot.py
   ```

5. Start the bot on Telegram by searching for your bot's username or clicking the link provided by BotFather.

## How it works

1. **/start Command**: When a user types `/start`, the bot welcomes them and provides instructions.
2. **/quiz Command**: To start the quiz, users type `/quiz`. The bot will send a random question with four answer options.
3. **Answering Questions**: Users respond by typing the number corresponding to their chosen option. The bot checks the answer, awards points for correct responses, and moves on to the next question.
4. **Quiz Completion**: When all questions are answered, the bot notifies the user that they've completed the quiz and allows them to start again.

## Hosting

This bot is hosted on [PythonAnywhere](https://www.pythonanywhere.com/), allowing it to run 24/7 and be accessible to anyone at any time.

## File Structure

- `quiz_bot.py`: Main script that runs the bot and handles all logic.
- `requirements.txt`: A file containing the necessary dependencies (if needed).

## License

This project is open-source and available under the [MIT License](LICENSE).

---

With this update, the bot link is clearly highlighted, and the hosting information via PythonAnywhere is included for easy access.

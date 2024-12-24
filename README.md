# Quiz Telegram Bot

This is a simple Telegram quiz bot built using Python and the `python-telegram-bot` library. It allows users to take a quiz with multiple-choice questions and tracks their points.

## Features
- Start the quiz with the `/start` command.
- Answer multiple-choice questions and earn points.
- View the final score after completing the quiz.
- Restart the quiz using the `/restart` command.

## Requirements
- Python 3.x
- `python-telegram-bot` library (can be installed via `pip install python-telegram-bot`)

## Installation

1. Clone this repository or download the script.
2. Install the required libraries:
   ```
   pip install python-telegram-bot
   ```
3. Replace `TOKEN` in the script with your own Telegram Bot API token.
4. Run the script:
   ```
   python quiz_bot.py
   ```

## Commands

### `/start`
- Resets the user's progress and welcomes them to the quiz bot.

### `/quiz`
- Starts the quiz by presenting the first question.

### `/restart`
- Restarts the quiz and resets the user's score.

## How It Works
- The bot starts by initializing the user data and presenting the first question.
- Each question has multiple options (shuffled) to choose from.
- The user sends their answer as a number (1-4), and the bot checks if the answer is correct.
- Points are awarded for each correct answer.
- The bot continues to the next question after each answer until all questions are answered.
- Once all questions are completed, the bot displays the total score.

## Example Interaction

1. **User**: `/start`  
   **Bot**: "Hello, Welcome to the quiz bot. Type /quiz to start the quiz."

2. **User**: `/quiz`  
   **Bot**: "Question 1: What is the capital of France?  
   1. Paris  
   2. London  
   3. Berlin  
   4. Madrid  
   Reply with the number of your answer."

3. **User**: `1`  
   **Bot**: "Correct answer! 🎉 You earned 10 points."

4. **User**: `/restart`  
   **Bot**: "The quiz has been restarted. Type /quiz to start again!"

## License
This project is open source and available under the MIT License.

## Acknowledgements
- `python-telegram-bot` library for Telegram bot interaction.

Enjoy the quiz!

from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import random
from flask import Flask, request

# Bot configuration
TOKEN: Final = '6911599717:AAFtGu8AMC8hBj83hxyYDzzVnYucT72EIHs'
BOT_USERNAME: Final = 'quizz_do_bot'
WEBHOOK_URL = f'https://quizbot-telegram-1.onrender.com/{TOKEN}'

# Data for the bot
user_data = {}
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["Paris", "London", "Berlin", "Madrid"],
        "correct_answer": "Paris",
        "points": 10
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Mars", "Venus", "Earth", "Jupiter"],
        "correct_answer": "Mars",
        "points": 10
    },
    {
        "question": "What is the largest mammal on Earth?",
        "options": ["Elephant", "Giraffe", "Blue Whale", "Lion"],
        "correct_answer": "Blue Whale",
        "points": 10
    },
    {
        "question": "What is the color of the sky on a clear day?",
        "options": ["Blue", "Green", "Red", "Yellow"],
        "correct_answer": "Blue",
        "points": 10
    },
    {
        "question": "Which animal is known as the King of the Jungle?",
        "options": ["Lion", "Tiger", "Elephant", "Bear"],
        "correct_answer": "Lion",
        "points": 10
    },
    {
        "question": "How many continents are there on Earth?",
        "options": ["5", "6", "7", "8"],
        "correct_answer": "7",
        "points": 10
    }
]

# Flask app setup
app = Flask(__name__)

# Telegram bot application
tg_app = Application.builder().token(TOKEN).build()

# Command handlers
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    user_data[chat_id] = {"current_question_index": 0, "points": 0}
    await update.message.reply_text('Hello! Welcome to the quiz bot. Type /quiz to start the quiz.')

async def quiz_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Quiz logic remains the same
    pass

async def answer_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Answer logic remains the same
    pass

async def restart_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    user_data[chat_id] = {"current_question_index": 0, "points": 0}
    await update.message.reply_text("Quiz restarted! Type /quiz to play again.")

# Adding handlers
tg_app.add_handler(CommandHandler('start', start_command))
tg_app.add_handler(CommandHandler('quiz', quiz_command))
tg_app.add_handler(CommandHandler('restart', restart_command))
tg_app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, answer_question))

# Flask route for webhook
@app.route(f'/{TOKEN}', methods=['POST'])
def handle_webhook():
    tg_app.update_queue.put(request.get_json(force=True))
    return "OK"

# Flask route for health check
@app.route('/health', methods=['GET'])
def health_check():
    return "I'm alive!"

# Run Flask app
if __name__ == '__main__':
    print("Starting Flask app for webhook...")
    app.run(host='0.0.0.0', port=5000)

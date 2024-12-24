
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import random

TOKEN: Final = '6911599717:AAFtGu8AMC8hBj83hxyYDzzVnYucT72EIHs'
BOT_USERNAME: Final = 'quizz_do_bot'

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

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    user_data[chat_id] = {"current_question_index": 0, "points": 0}  # Reset user data
    await update.message.reply_text('Hello, Welcome to the quiz bot. Type /quiz to start the quiz.')

async def quiz_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    user = user_data.get(chat_id)

    if user:
        current_question_index = user["current_question_index"]
        if current_question_index < len(quiz_data):
            question_data = quiz_data[current_question_index]
            question = question_data["question"]
            options = question_data["options"]

            random.shuffle(options)
            user_data[chat_id]["correct_answer"] = question_data["correct_answer"]

            reply_text = f"Question {current_question_index + 1}: {question}\n\n"
            for i, option in enumerate(options):
                reply_text += f"{i + 1}. {option}\n"
            reply_text += "\nReply with the number of your answer."

            await update.message.reply_text(reply_text)
        else:
            points = user["points"]
            await update.message.reply_text(f"You have completed the quiz with a score of {points} points! 🎉\nType /restart to play again.")
    else:
        await update.message.reply_text("Please start the quiz with /start.")

async def answer_question(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    user = user_data.get(chat_id)

    if user:
        current_question_index = user["current_question_index"]
        if current_question_index < len(quiz_data):
            try:
                chosen_option = int(update.message.text)
                correct_answer = user["correct_answer"]

                if 1 <= chosen_option <= 4:
                    options = quiz_data[current_question_index]["options"]
                    if options[chosen_option - 1] == correct_answer:
                        points = quiz_data[current_question_index]["points"]
                        user_data[chat_id]["points"] += points
                        await update.message.reply_text(f"Correct answer! 🎉 You earned {points} points.")
                    else:
                        await update.message.reply_text("Wrong answer. 😔")
                    user_data[chat_id]["current_question_index"] += 1
                    await quiz_command(update, context)
                else:
                    await update.message.reply_text("Please choose a valid option (1-4).")
            except ValueError:
                await update.message.reply_text("Please enter a valid number (1-4).")
            except Exception as e:
                await update.message.reply_text(f"An error occurred: {str(e)}")
                print(f"Error in answer_question: {str(e)}")
        else:
            await update.message.reply_text("You have already completed the quiz. Type /restart to play again.")
    else:
        await update.message.reply_text("Please start the quiz with /start.")

async def restart_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.message.chat_id
    user_data[chat_id] = {"current_question_index": 0, "points": 0}  # Reset user data
    await update.message.reply_text("The quiz has been restarted. Type /quiz to start again!")

if __name__ == '__main__':
    print("Starting bot...")
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('quiz', quiz_command))
    app.add_handler(CommandHandler('restart', restart_command))  # Added restart handler
    app.add_handler(MessageHandler(filters.TEXT, answer_question))

    print('Polling')
    app.run_polling(poll_interval=3)

import os
import telebot

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello! Your bot is now connected and working!")

@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(message, f"You said: {message.text}")

print("Bot is running...")

bot.polling(none_stop=True)
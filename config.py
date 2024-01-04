from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

from dotenv import load_dotenv
import requests
import os

load_dotenv()

class Bot:
    def __init__(self):
        self.TOKEN = os.getenv("TOKEN")
        self.bot = ApplicationBuilder().token(self.TOKEN).build()

    async def hello(update: Update, contex: ContextTypes.DEFAULT_TYPE) -> None:
        await update.message.reply_text(f'Hello {update.effective_user.first_name}')

    def run(self):
        self.bot.add_handler(CommandHandler("hello", self.hello))

        self.bot.run_polling()

"""
def main():
    pandorabot = ApplicationBuilder().token(TOKEN).build()

    pandorabot.add_handler(CommandHandler("hello", hello))
    
    pandorabot.run_polling()
"""


if __name__ == "__main__":
    pandora = Bot()
    pandora.run()

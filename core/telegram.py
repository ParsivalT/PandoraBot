import telebot
from time import sleep
import sys
from config import TOKEN, LOG
from utils.youtube_download import youtube2mp3
import core.messages as Messages

bot = telebot.TeleBot(TOKEN)

# Variável global para controlar a execução do bot
is_running = True

@bot.message_handler(commands=["menu"])
def menu(message):
    bot.reply_to(message, "**OI**, como voce esta ", parse_mode="Markdown")


@bot.message_handler(commands=["shutdown"])
def shutdown(message):
    global is_running
    is_running = False
    bot.reply_to(message, "Bot está sendo desligado...")
    sys.exit("Bot encerrado forcadamente")


@bot.message_handler(commands=["get_mp3"])
def get_mp3(message):
    url = message.text[9:]

    youtube2mp3(url, bot=bot, message=message)

def run():
    print("[~] Telegram Bot starting...")
    try:    
        print("[?] Started as @" + bot.get_me().username)
    except Exception as error:
        exit(f"[!] Failed connect to telegram bot\n{error}")
    else:
        while is_running:
            try:
                bot.polling(none_stop=True)
            except Exception as error:
                print(error)
                sleep(2)
    print("[!] Telegram Bot has been stopped.")
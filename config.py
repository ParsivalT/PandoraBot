# Telegram Modulos
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Modulos para gerenciamento.
import logging
from dotenv import load_dotenv
import os

import requests

# Configurando o Formato de Exibição dos Logs e Instanciando a Classe.
LOG_FORMAT = 'Data/Hora: %(asctime)s | LEVEL:%(levelname)s | Mensagem:%(message)s'
logging.basicConfig(filename="relatorio.log", level=logging.INFO, format=LOG_FORMAT)
LOG = logging.getLogger()

# Crregando as Variaveis de Ambiente.
load_dotenv()

# Classe Principal, para interagir de maneira mais facil com o modulo do Telegram.
class Bot:
    def __init__(self):
        # Carregando o TOKEN e instanciando a classe.
        self.TOKEN = os.getenv("TOKEN")
        self.bot = ApplicationBuilder().token(self.TOKEN).build()



    async def hello(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """
            Example: 

            In: /hello

            Out: Hello, Parsival
        """
        await update.message.reply_text(f'Hello {update.effective_user.first_name}')
        LOG.info(update.effective_user)


    # Função para iniciar o Bot.
    def run(self):
        self.bot.add_handler(CommandHandler("hello", self.hello))

        self.bot.run_polling()

if __name__ == "__main__":
    pandora = Bot()
    pandora.run()
    
"""
def main():
    pandorabot = ApplicationBuilder().token(TOKEN).build()

    pandorabot.add_handler(CommandHandler("hello", hello))
    
    pandorabot.run_polling()
"""

# Telegram Modulos
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Modulos para gerenciamento.
import logging
import datetime 
from dotenv import load_dotenv
import os
import tempfile

import requests

# Configurando o Formato de Exibição dos Logs e Instanciando a Classe.
LOG_FORMAT = 'Data/Hora: %(asctime)s | LEVEL:%(levelname)s | Mensagem:%(message)s'
logging.basicConfig(filename="relatorio.log", level=logging.DEBUG, format=LOG_FORMAT)
LOG = logging.getLogger()

# Crregando as Variaveis de Ambiente.
load_dotenv()

TOKEN = os.getenv("TOKEN")
# Modulo responsavel por Gerenciar o funcionamento do BOT
from core.utils import *

# Função para facilitar a ultilização do telegram-bot
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


    async def coffer(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        try: 
            data = requests.get("https://coffee.alexflipnote.dev/random.json").json()
            file_url = data['file']

            await update.message.reply_photo(photo=file_url)
    
        except:
            await update.message.reply_text("Estou com Problemas Para cessar a api")
            LOG.warning('API COFFER offiline.')


    async def crypto(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        LOG.warning("Entrei na API")
        API = CoinGeckoAPI(url_base='https://api.coingecko.com/api/v3')
        
        try:
            mensagem = []
            
            # Supondo que 'atualizado_em' seja obtido de algum lugar
            atualizado_em = datetime.datetime.now().timestamp()
            data_hora = datetime.datetime.fromtimestamp(atualizado_em).strftime('%x %X')

            preco, _ = API.consulta_preco(id_moeda='bitcoin')
            preço_dolar, variacao = dolar()
            
            mensagem.append(f'*Últimas Atualizações*')
            mensagem.append(f'*Cotação do Dólar:* \n\t*Preço*: R$ {preço_dolar:.2f}' \
                            f'\n\t*Variação de:* {variacao}%')
            mensagem.append(f'*Cotação do Bitcoin*: \n\t*Preço*: R$ {preco:,.2f}' \
                            f'\n\t*Horário*: {data_hora}\n\t')
            
            for men in mensagem:
                print(men)
                await update.message.reply_markdown(text=men)

        except ConnectionError as err:
            print("DEU ERRO")
            await update.message.reply_text(text=str(err))


    # Função para iniciar o Bot.
    def run(self):

        self.bot.add_handler(CommandHandler("hello", self.hello))
        self.bot.add_handler(CommandHandler("coffer", self.coffer))
        self.bot.add_handler(CommandHandler("btcprice", self.crypto))

        self.bot.run_polling()
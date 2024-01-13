from pytube import YouTube
from pathlib import Path
import shutil
import config 

def youtube2mp3(url, bot, message):
    # URL de entrada do usuário

    chat_id = message.chat.id

    # Criar um diretório temporário
    temp_dir = config.tempfile.mkdtemp()

    try:
        yt = YouTube(url)
        # Baixar o arquivo

        # Extrair áudio com qualidade de 160kbps do vídeo
        bot.reply_to(message, "Iniciando Download")
        video = yt.streams.filter(abr='160kbps').last()

        out_file = video.download(output_path=temp_dir)
        base, ext = config.os.path.splitext(out_file)
        new_file = Path(f'{base}.mp3')
        config.os.rename(out_file, new_file)

        # Enviar o arquivo para o Telegram
        with open(new_file, 'rb') as audio_file:
            bot.send_chat_action(chat_id, "upload_audio")
            bot.send_audio(chat_id=chat_id, audio=audio_file)

        # Verificar o sucesso do envio
        sent_message = bot.send_message(chat_id, f'{yt.title} Aproveite o Som.')

    except Exception as err:
        bot.reply_to(message, "Houve um problema", parse_mode="Markdown")

    finally:
        # Limpar o diretório temporário quando terminar de usar
        print('Limpando diretório temporário...')
        shutil.rmtree(temp_dir)


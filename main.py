from gtts import gTTS
from playsound import playsound

audio = 'audio.mp3'  # nome do arquivo que vai ser gerado
linguagem = 'pt-br'  # linguagem que vai ser gerado o áudio

sp = gTTS(
    # texto  que vai ser transformando em áudio
    text='meu primeiro áudio gerado com python',
    lang=linguagem
)

sp.save(audio)
playsound(audio)

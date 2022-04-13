import gtts
from playsound import playsound
from time import sleep

with open('frase.txt', 'r') as file:
    for line in file:
        mySound = gtts.gTTS(line,lang='pt-BR')
        mySound.save('talktome.mp3')
        sleep(5)
        playsound('talktome.mp3')

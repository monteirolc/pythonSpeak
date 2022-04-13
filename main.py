import gtts
from playsound import playsound

with open('frase.txt', 'r') as file:
    for line in file:
        mySound = gtts.gTTS(line,lang='pt-br')
        mySound.save('speak.mp3')
        playsound('speak.mp3')

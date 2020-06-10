from pygame import mixer
from time import sleep

mixer.init()

mixer.music.load("C:/Users/Usuário/Music/aides_crew_tua_mãe_é_uma_cadela.mp3")
mixer.music.play()

sleep(5)

mixer.quit()
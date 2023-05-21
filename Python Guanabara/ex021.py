from pygame import init, mixer, time, event
from pygame.locals import *

init()

mixer.music.set_volume(0.5)
mixer.music.load('BoxCat Games - Tricks.mp3')
mixer.music.play(-1)

relogio = time.Clock()
event.wait()

while True:
    relogio.tick(30)

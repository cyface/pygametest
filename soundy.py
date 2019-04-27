import pygame
import time
import gpiozero

# pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
pygame.mixer.init()

soundObj = pygame.mixer.Sound('laser.wav')
soundObj.play()

button = gpiozero.Button(23)
while True:
    if button.is_pressed:
        print("Pressed")
        soundObj.play()
        time.sleep(.25)  # wait and let the sound play for X second

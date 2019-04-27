import pygame
import time

#pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
pygame.mixer.init()

soundObj = pygame.mixer.Sound('laser.wav')
soundObj.play()
time.sleep(1) #wait and let the sound play for X second
soundObj.stop()

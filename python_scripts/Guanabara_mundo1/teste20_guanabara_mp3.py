import pygame
pygame.init()
pygame.mixer.music.load('chipi.mp3') # o arquivo precisa estar dentro da pasta do projeto
pygame.mixer.music.play()
input()
pygame.event.wait()

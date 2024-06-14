#Faça um programa que toque uma música

import pygame
pygame.init()
pygame.mixer.music.load('desafio20.mp3') # o arquivo precisa estar noprojeto
pygame.mixer.music.play()
input()
pygame.event.wait()

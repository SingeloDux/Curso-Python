# Faca um progrma em python que abra e reproduza o audio de um arquivo MP3

import pygame
pygame.init()
pygame.mixer.music.load('easier2run.mp3')
pygame.mixer.music.play()
pygame.event.wait()
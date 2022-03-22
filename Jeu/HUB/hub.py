import pygame, sys
from pygame.locals import *
pygame.init()

# Création de la fenetre + fond
pygame.display.set_caption("ArtSoliStone")
screen = pygame.display.set_mode((1080, 720))
background = pygame.image.load('img/fond.png')
text = pygame.image.load('img/text.png')
jouer = pygame.image.load('img/bouton.png')

#Ajoute de la musique de fond
music = 'music/fond.mp3'
pygame.mixer.init()
pygame.mixer.music.load(music)
pygame.mixer.music.play(-1)

running = True

while running:
    screen.blit(background, (0, 0))
    screen.blit(text, (270, 30))
    screen.blit(jouer, (370, 350))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
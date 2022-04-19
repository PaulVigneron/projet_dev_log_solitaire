import math
import pygame
import os
from pygame.locals import *
from hub import *

pygame.init()

# Création de la fenetre + fond
pygame.display.set_caption("ArtSoliStone")
screen = pygame.display.set_mode((1080, 720))

# importer le fond
background = pygame.image.load('./img/fond.png')

# importer le logo
text = pygame.image.load('./img/text.png')
text = pygame.transform.scale(text,(600, 400))
text_rect = text.get_rect()
text_rect.x = math.ceil(screen.get_width() / 4)
text_rect.y = math.ceil(screen.get_height() / 5)

# importer le bouton jouer
play_button = pygame.image.load('./img/bouton.png')
play_button = pygame.transform.scale(play_button, (300, 300))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33)
play_button_rect.y = math.ceil(screen.get_height() / 2)


clickable_area = pygame.Rect((220, 377), (149,66))
rect_surf = pygame.Surface(clickable_area.size)

# importer les reseaux
reseau = pygame.image.load('./img/reseau.png')

#Ajoute de la musique de fond
music = './music/fond.mp3'
pygame.mixer.init()
pygame.mixer.music.load(music)
pygame.mixer.music.play(-1)

running = True


# boucle tant que cette condition est vrai
while running:

    # appliquer le fond, reseaux et le logo
    screen.blit(background, (0, 0))
    screen.blit(text, (270, 30))
    screen.blit(reseau, (830, 0))
    screen.blit(play_button, (370, 350))

    pygame.display.flip()

    # si le joueur ferme la fenetre
    for event in pygame.event.get():
        # que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
        #elif event.type == pygame.KEYDOWN:
         #   hub.pressed[event.key] = True
        #elif event.type == pygame.KEYUP:
         #   hub.pressed[event.key] = False

#        elif event.type == pygame.MOUSEBUTTONUP:
            # verif pour savoir si la sourie est en collision avec le bouton play
#            if play_button_rect.collidepoint(event.pos):
#                exec(open("hub.py").read())
#               running = False

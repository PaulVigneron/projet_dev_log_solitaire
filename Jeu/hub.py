import math
import pygame
import os
from pygame.locals import *
import moviepy.editor
pygame.init()

    # Création de la fenetre + fond
pygame.display.set_caption("ArtSoliStone")
screen = pygame.display.set_mode((1080, 720))



# importer le fond
background = moviepy.editor.VideoFileClip('./img/fond_menu.mp4')
background.preview()

# importer la bande en bas
barre = pygame.image.load('./img/fond_hub.png')

running = True

while running:

    screen.blit(background, (0, 0))
    screen.blit(barre, (270, 30))

    pygame.display.flip()

    # si le joueur ferme la fenetre
    for event in pygame.event.get():
        # que l'evenement est fermeture de fenetre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeu")
import pygame
from obj.Window import Window
from Solitaire.obj.Cards import Cards
import obj.constants as constants

pygame.init()

# Create Window
window = Window()
cards = Cards()

# Game execution
while window.running:

    # Apply background to window
    window.screen.blit(window.background, (0, 0))
    window.screen.blit(pygame.image.load(cards.card_list[45].image_file_name), (30, 550))
    pygame.display.flip()

    # Quit the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window.quit()

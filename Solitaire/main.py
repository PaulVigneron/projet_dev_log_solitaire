import pygame
from pygame.locals import *
from obj.Window import Window
pygame.init()

# Create Window
window = Window()

# Game execution
while window.running:

    # Apply background to window
    window.reload()

    # Quit the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            window.quit()

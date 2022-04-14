import arcade
from Solitaire.obj.Window import Window

# Create and run window
window = Window()
window.setup()
arcade.run()

# import pygame
# from obj.Window import Window
# from Solitaire.obj.Cards import Cards
# import obj.constants as constants
#
# pygame.init()
#
# # Create Window
# window = Window()
# cards = Cards()
# window.screen.blit(window.background, (0, 0))
# window.screen.blit(pygame.image.load(cards.card_list[0].image_file_name), (30, 550))
#
# # Game execution
# while window.running:
#
#     # Apply background to window
#
#
#     # Show Card to the user
#     # window.screen.blit(pygame.image.load(cards.card_list[0].image_file_name), (30, 550))
#
#     # Quit the window
#     for event in pygame.event.get():
#
#         if event.type == pygame.MOUSEBUTTONUP:
#             cards.draw(window, 0)
#         pygame.display.flip()
#
#         if event.type == pygame.QUIT:
#             window.quit()

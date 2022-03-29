import pygame


class Window:

    def __init__(self):
        self.screen_title = "ArtSoliStone"
        self.screen_width = 1080
        self.screen_height = 720
        self.running = True
        self.background = pygame.image.load('./assets/background.jpeg')
        self.background = pygame.transform.scale(self.background, (1080, 720))
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption(self.screen_title)

    # Close window
    def quit(self):
        self.running = False
        print("Game closed !")
        pygame.quit()

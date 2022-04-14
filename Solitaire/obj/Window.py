import arcade
import Solitaire.obj.constants as constants
from Solitaire.obj.Card import Card


class Window(arcade.Window):

    def __init__(self):
        super().__init__(constants.screen_width, constants.screen_height, constants.screen_title)

        self.card_list = None

        # Background color
        arcade.set_background_color(arcade.color.AMAZON)

        # List of cards we held with mouse
        self.held_cards = None

        # List of cards position
        self.held_cards_initial_position = None

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """

        # List of cards we held with mouse
        self.held_cards = []

        # List of cards position
        self.held_cards_initial_position = []

        self.card_list = arcade.SpriteList()

        for card_suit in constants.card_suits:
            for card_value in constants.card_values:
                card = Card(card_suit, card_value)
                card.position = constants.START_X, constants.BOTTOM_Y
                self.card_list.append(card)

    def on_draw(self):
        """ Render the screen. """
        # Clear the screen
        arcade.start_render()

        # Draw the cards
        self.card_list.draw()

    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """

        # Get cards we clicked on
        cards = arcade.get_sprites_at_point((x, y), self.card_list)

        if len(cards) > 0:
            # Get first card of the pile
            first_card = cards[-1]

            # Gab the face up card we clicked on, save its position and put it on top to draw it first
            self.held_cards = [first_card]
            self.held_cards_initial_position = [self.held_cards[0].position]
            self.pull_to_top(self.held_cards[0])

    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        """ Called when the user presses a mouse button. """

        # Do nothing if we don't have cards
        if len(self.held_cards) == 0:
            return

        # Drop the cards
        self.held_cards = 0

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """ User moves mouse """

        # If cards are held, move with them
        for card in self.held_cards:
            card.center_x += dx
            card.center_y += dy

    def pull_to_top(self, card: arcade.Sprite):
        self.card_list.remove(card)
        self.card_list.append(card)

        # self.screen_title = "ArtSoliStone"
        # self.screen_width = 1080
        # self.screen_height = 720
        # self.running = True
        # self.background = pygame.image.load('./assets/background.jpeg')
        # self.background = pygame.transform.scale(self.background, (1080, 720))
        # self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        # pygame.display.set_caption(self.screen_title)

    # # Close window
    # def quit(self):
    #     self.running = False
    #     print("Game closed !")
    #     pygame.quit()

import arcade
import random
import Solitaire.obj.constants as constants
from Solitaire.obj.Card import Card


class Window(arcade.Window):

    def __init__(self):
        super().__init__(constants.screen_width, constants.screen_height, constants.screen_title)

        # List of cards
        self.card_list = None

        # Background color
        arcade.set_background_color(arcade.color.AMAZON)

        # List of cards we held with mouse
        self.held_cards = None

        # List of cards position
        self.held_cards_initial_position = None

        # List with all the slots for the cards
        self.pile_slot_list = None

        # List of lists, one for each pile
        self.piles = None

    def setup(self):
        """ Set up the game here. Call this function to restart the game. """

        # List of cards we held with mouse
        self.held_cards = []

        # List of cards position
        self.held_cards_initial_position = []

        # --- Creating slots for cards

        # Sprite list with all the slots
        self.pile_slot_list: arcade.SpriteList = arcade.SpriteList()

        # Bottom slots (2 slots)
        pile = arcade.SpriteSolidColor(constants.slot_width, constants.slot_height, arcade.csscolor.DARK_OLIVE_GREEN)
        pile.position = constants.start_x, constants.bottom_y
        self.pile_slot_list.append(pile)

        pile = arcade.SpriteSolidColor(constants.slot_width, constants.slot_height, arcade.csscolor.DARK_OLIVE_GREEN)
        pile.position = constants.start_x + constants.x_spacing, constants.bottom_y
        self.pile_slot_list.append(pile)

        # Middle slots (7 slots)
        for i in range(7):
            pile = arcade.SpriteSolidColor(
                constants.slot_width,
                constants.slot_height,
                arcade.csscolor.DARK_OLIVE_GREEN
            )
            pile.position = constants.start_x + i * constants.x_spacing, constants.middle_y
            self.pile_slot_list.append(pile)

        # Top slots (4 slots)
        for i in range(4):
            pile = arcade.SpriteSolidColor(
                constants.slot_width,
                constants.slot_height,
                arcade.csscolor.DARK_OLIVE_GREEN
            )
            pile.position = constants.start_x + i * constants.x_spacing, constants.top_y
            self.pile_slot_list.append(pile)

        # --- Create shuffled deck

        # Sprite list with all the cards
        self.card_list = arcade.SpriteList()

        # Create all cards
        for card_suit in constants.card_suits:
            for card_value in constants.card_values:
                card = Card(card_suit, card_value)
                card.position = constants.start_x, constants.bottom_y
                self.card_list.append(card)

        # Shuffle the cards
        for pos1 in range(len(self.card_list)):
            pos2 = random.randrange(len(self.card_list))
            self.card_list.swap(pos1, pos2)

        # Create a list with all piles in it
        self.piles = [[] for _ in range(constants.pile_count)]

        # Put all cards in bottom face down pile
        for card in self.card_list:
            self.piles[constants.bottom_face_down_pile].append(card)

        # Deal cards on board
        for pile_no in range(constants.play_pile_1, constants.play_pile_7 + 1):
            for j in range(pile_no - constants.play_pile_1 + 1):
                card = self.piles[constants.bottom_face_down_pile].pop()
                self.piles[pile_no].append(card)
                card.position = self.pile_slot_list[pile_no].position
                self.pull_to_top(card)

        for i in range(constants.play_pile_1, constants.play_pile_7 + 1):
            self.piles[i][-1].face_up()

    def on_draw(self):
        """ Render the screen. """
        # Clear the screen
        arcade.start_render()

        # Draw slots
        self.pile_slot_list.draw()

        # Draw the cards
        self.card_list.draw()

    def on_mouse_press(self, x, y, button, key_modifiers):
        """ Called when the user presses a mouse button. """

        # Get cards we clicked on
        cards = arcade.get_sprites_at_point((x, y), self.card_list)

        if len(cards) > 0:
            # Get first card of the pile
            first_card = cards[-1]
            assert isinstance(first_card, Card)

            pile_index = self.get_pile_for_card(first_card)

            if pile_index == constants.bottom_face_down_pile:
                for i in range(3):
                    if len(self.piles[constants.bottom_face_down_pile]) == 0:
                        break
                    card = self.piles[constants.bottom_face_down_pile][-1]
                    card.face_up()
                    card.position = self.pile_slot_list[constants.bottom_face_up_pile].position
                    self.piles[constants.bottom_face_down_pile].remove(card)
                    self.piles[constants.bottom_face_up_pile].append(card)
                    self.pull_to_top(card)

            elif first_card.is_face_down:
                first_card.face_up()

            else:
                # Gab the face up card we clicked on, save its position and put it on top to draw it first
                self.held_cards = [first_card]
                self.held_cards_initial_position = [self.held_cards[0].position]
                self.pull_to_top(self.held_cards[0])
                card_index = self.piles[pile_index].index(first_card)
                for i in range(card_index + 1, len(self.piles[pile_index])):
                    card = self.piles[pile_index][i]
                    self.held_cards.append(card)
                    self.held_cards_initial_position.append(card.position)
                    self.pull_to_top(card)

        else:
            # If we clicked on a slot instead of card
            slots = arcade.get_sprites_at_point((x, y), self.pile_slot_list)
            if len(slots) > 0:
                slot = slots[0]
                slot_index = self.pile_slot_list.index(slot)
                # If there is no card on deck pile
                if slot_index == constants.bottom_face_down_pile and len(self.piles[constants.bottom_face_down_pile]) == 0:
                    temp_list = self.piles[constants.bottom_face_up_pile].copy()
                    for card in reversed(temp_list):
                        card.face_down()
                        self.piles[constants.bottom_face_up_pile].remove(card)
                        self.piles[constants.bottom_face_down_pile].append(card)
                        card.position = self.pile_slot_list[constants.bottom_face_down_pile].position

    # TODO: card release on original slot create bugs if its position was reset before.
    #  Check what happens on mouse release, maybe Mac problem.
    def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
        """ Called when the user presses a mouse button. """

        # Do nothing if we don't have cards
        if len(self.held_cards) == 0:
            return

        # Find the closest pile
        pile, distance = arcade.get_closest_sprite(self.held_cards[0], self.pile_slot_list)
        reset_position = True

        # Check if we're in contact with the closest pile
        if arcade.check_for_collision(self.held_cards[0], pile):

            # What pile are we aiming
            pile_index = self.pile_slot_list.index(pile)

            # If it's the same pile
            if pile_index == self.get_pile_for_card(self.held_cards[0]):
                # Just continue
                pass

            elif constants.play_pile_1 <= pile_index <= constants.play_pile_7:
                # Are there already cards here
                if len(self.piles[pile_index]) > 0:
                    # Move cards to position
                    top_card = self.piles[pile_index][-1]
                    for i, dropped_card in enumerate(self.held_cards):
                        dropped_card.position = top_card.center_x, \
                                                top_card.center_y - constants.card_vertical_gap * (i + 1)
                else:
                    # If there is no cards
                    for i, dropped_card in enumerate(self.held_cards):
                        # Move cards to position
                        dropped_card.position = pile.center_x, \
                                                pile.center_y - constants.card_vertical_gap * i

                for card in self.held_cards:
                    # Cards are in the right position, but we need to move them to the right list
                    self.move_card_to_new_pile(card, pile_index)

                # On success, don't reset card position
                reset_position = False

            elif constants.top_pile_1 <= pile_index <= constants.top_pile_4 and len(self.held_cards) == 1:
                # Move position of card to pile
                self.held_cards[0].position = pile.position
                # Move card to card list
                for card in self.held_cards:
                    self.move_card_to_new_pile(card, pile_index)

                reset_position = False

        # If we drop on invalid position
        if reset_position:
            # Reset cards in initial position
            for pile_index, card in enumerate(self.held_cards):
                card.position = self.held_cards_initial_position[pile_index]

        # Drop the cards
        self.held_cards = []

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        """ User moves mouse """

        # If cards are held, move with them
        for card in self.held_cards:
            card.center_x += dx
            card.center_y += dy

    def pull_to_top(self, card: arcade.Sprite):
        """ Pull card to top of rendering order (last to render, looks on-top) """

        self.card_list.remove(card)
        self.card_list.append(card)

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.R:
            self.setup()

    def get_pile_for_card(self, card):
        """ What pile is this card in? """

        for index, pile in enumerate(self.piles):
            if card in pile:
                return index

    def remove_card_from_pile(self, card):
        """ Remove card from whatever pile it was in. """

        for pile in self.piles:
            if card in pile:
                pile.remove(card)
                break

    def move_card_to_new_pile(self, card, pile_index):
        """ Move the card to a new pile """

        self.remove_card_from_pile(card)
        self.piles[pile_index].append(card)

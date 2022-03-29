class Card:

    def __init__(self, suit, value):

        self.suit = suit
        self.value = value
        # Image to use for the sprite when face up
        self.image_file_name = f"./assets/cards/{self.suit}{self.value}.png"

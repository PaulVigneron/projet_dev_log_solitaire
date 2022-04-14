import arcade


class Card(arcade.Sprite):

    def __init__(self, suit, value, scale=1):

        self.suit = suit
        self.value = value

        # Image to use for the sprite when face up
        self.image_file_name = f"./assets/cards/{self.suit}{self.value}.png"

        super().__init__(self.image_file_name, scale, hit_box_algorithm="None")

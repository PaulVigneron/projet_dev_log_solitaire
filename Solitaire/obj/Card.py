import arcade


class Card(arcade.Sprite):

    def __init__(self, suit, value, scale=1):

        self.suit = suit
        self.value = value

        # Image to use for the sprite when face up
        self.image_file_name = f"./assets/cards/{self.suit}{self.value}.png"

        # Image to use for the sprite when face down
        self.card_back = f"./assets/card_back.png"
        self.is_face_up = False

        super().__init__(self.card_back, scale, hit_box_algorithm="None")

    def face_down(self):
        self.texture = arcade.load_texture(self.card_back)
        self.is_face_up = False

    def face_up(self):
        self.texture = arcade.load_texture(self.image_file_name)
        self.is_face_up = True

    @property
    def is_face_down(self):
        return not self.is_face_up

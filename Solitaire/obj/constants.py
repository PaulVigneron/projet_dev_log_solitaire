# Window params
screen_width = 1080
screen_height = 720
screen_title = "ArtSoliStone"

# Card values
card_values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
card_suits = ["Clubs", "Hearts", "Spades", "Diamonds"]

# Card size constant
card_scale = 0.6

# Card size
card_width = 140 * card_scale
card_height = 190 * card_scale

# Slot's size
card_slot_oversize = 1.25
slot_height = int(card_height * card_slot_oversize)
slot_width = int(card_width * card_slot_oversize)

# Space between slots
vertical_margin_scale = 0.10
horizontal_margin_scale = 0.10

# TODO: Rename + manipulate
# The Y of the bottom row (2 piles)
BOTTOM_Y = slot_height / 2 + slot_height * vertical_margin_scale * 2

# The X of where to start putting things on the left side
START_X = slot_width / 2 + slot_width * horizontal_margin_scale

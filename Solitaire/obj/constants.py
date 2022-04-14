# Window params
screen_width = 1024
screen_height = 768
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
card_slot_oversize = 1
slot_height = int(card_height * card_slot_oversize)
slot_width = int(card_width * card_slot_oversize)

# Space between slots
vertical_margin_scale = 0.10
horizontal_margin_scale = 0.10

# The X of where to start putting things on the left side
start_x = slot_width / 2 + slot_width * horizontal_margin_scale

# The Y of the bottom row (2 piles)
bottom_y = slot_height / 2 + slot_height * vertical_margin_scale

# The Y of the top row (4 piles)
top_y = screen_height - slot_height / 2 - slot_height * vertical_margin_scale

# The Y of the middle row (7 piles)
middle_y = top_y - slot_height - slot_height * vertical_margin_scale

# TODO: How far apart each pile goes
x_spacing = slot_height + slot_width * horizontal_margin_scale / 2


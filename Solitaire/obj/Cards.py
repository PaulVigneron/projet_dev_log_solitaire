from Solitaire.obj import constants
from Solitaire.obj.Card import Card


class Cards:

    def __init__(self):
        self.card_list = []

        for card_suit in constants.card_suits:
            for card_value in constants.card_values:
                card = Card(card_suit, card_value)
                self.card_list.append(card)

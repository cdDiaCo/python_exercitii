

class Deck :
    def __init__(self):
        self.cards = set()


    def shuffle_cards(self):
        pass


    def sort_cards(self):
        pass


    def add_card(self):
        pass


    def remove_card(self):
        pass




class Card :
    def __init__(self, card_number, card_color):
        self.card_number = card_number
        self.card_color = card_color
        pass


    def get_card_color(self):
        return self.card_color


    def get_card_number(self):
        return self.card_number




class Hand :
    def __init__(self, cards):
        self.cards = cards
        pass









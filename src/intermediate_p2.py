import random


class Deck :
    def __init__(self):
        self.cards = []

        colors = ["SPADES", "HEARTS", "DIAMONDS", "CLUBS"]
        for color in colors :
            for elem in range(2,16) :
                if elem == 11 :
                    continue
                new_card = (elem, color)
                self.add_card(new_card)


    def shuffle_cards(self):
        middle = int(len(self.cards)/2)
        num_of_cards = len(self.cards)

        for i in range(1, middle):
            first_random_card_position = random.randint(1, middle)
            second_random_card_position = random.randint(middle+1, num_of_cards-1)
            temp = self.cards[first_random_card_position]
            self.cards[first_random_card_position] = self.cards[second_random_card_position]
            self.cards[second_random_card_position] = temp


    def sort_cards_by_number(self):
        def sortSecond(val):
            return val[0]

        new_deck.cards.sort(key=sortSecond)


    def sort_cards_by_color(self):
        def sortFirst(val):
            return val[1]

        new_deck.cards.sort(key=sortFirst)



    def add_card(self, card):
        # check if card already exists?
        self.cards.append(card)


    def remove_card(self, card):
        self.cards.remove(card)





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





new_deck = Deck()

#print(len(new_deck.cards))
#new_deck.shuffle_cards()
#print(new_deck.cards)

#new_deck.sort_cards_by_color()
#new_deck.sort_cards_by_number()


#print(new_deck.cards)

card = (3, 'SPADES')

#new_deck.remove_card(card)


print(new_deck.cards)

#new_deck.add_card(card)

#print("-----------------")
#print(new_deck.cards)


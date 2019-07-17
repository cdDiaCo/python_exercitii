

from collections import UserList
import random




class Deck(UserList) :

    def __init__(self):
        UserList.__init__(self)
        colors = ["SPADES", "HEARTS", "DIAMONDS", "CLUBS"]
        for color in colors :
            for num in range(2,16) :
                if num == 11 :
                    continue
                new_card = (num, color)
                self.add_card(new_card)



    def shuffle_cards(self):
        middle = int(len(self)/2)
        num_of_cards = len(self)

        for i in range(1, middle):
            first_random_card_position = random.randint(1, middle)
            second_random_card_position = random.randint(middle+1, num_of_cards-1)
            temp = self[first_random_card_position]
            self[first_random_card_position] = self[second_random_card_position]
            self[second_random_card_position] = temp



    def sort_cards_by_number(self):
        def sortSecond(val):
            return val[0]

        new_deck.sort(key=sortSecond)



    def sort_cards_by_color(self):
        def sortFirst(val):
            return val[1]

        new_deck.sort(key=sortFirst)



    def add_card(self, card):
        # check if card already exists?
        if card in self:
            print('Card already in deck.')
        else:
            self.append(card)



    def remove_card(self, card):
        if card in self:
            self.remove(card)
        else:
            print("Card cannot be removed. Card not present in deck")





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


class Player :
    def __init__(self):
        pass


class Table :
    def __init__(self):
        pass


class Dealer :
    def __init__(self):
        pass




new_deck = Deck()


#print(new_deck)
#new_deck.shuffle_cards()
#print(new_deck)

#new_deck.sort_cards_by_color()
#new_deck.sort_cards_by_number()



card = (3, 'SPADES')

new_deck.remove_card(card)

new_deck.remove_card(card)


#new_deck.add_card(card)

print(new_deck)




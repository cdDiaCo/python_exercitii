

from collections import UserList
import random




class Deck(UserList) :

    def __init__(self):
        UserList.__init__(self)


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



class HandDeck(Deck):
    def __init__(self):
        Deck.__init__(self)


    def add_card(self, card):
        if len(self) >= 2 :
            print("HandDeck can have max. two cards")
        else :
            super(HandDeck, self).add_card(card)



class DealerDeck(Deck):
    def __init__(self):
        Deck.__init__(self)
        colors = ["SPADES", "HEARTS", "DIAMONDS", "CLUBS"]
        for color in colors:
            for num in range(2, 16):
                if num == 11:
                    continue
                new_card = Card(num, color)
                self.add_card(new_card)


    def shuffle_cards(self):
        middle = int(len(self) / 2)
        num_of_cards = len(self)

        for i in range(1, middle):
            first_random_card_position = random.randint(1, middle)
            second_random_card_position = random.randint(middle + 1, num_of_cards - 1)
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



class TableDeck(Deck):
    def __init__(self):
        Deck.__init__(self)


    def add_card(self, card):
        if len(self) >= 5 :
            print("TableDeck can have max. five cards")
        else :
            super(TableDeck, self).add_card(card)



class Card :
    def __init__(self, card_number, card_color):
        self.card_number = card_number
        self.card_color = card_color
        pass


    def get_card_color(self):
        return self.card_color


    def get_card_number(self):
        return self.card_number





class Hand() :
    def __init__(self):
        self.hand_deck = HandDeck()



class Player :
    def __init__(self):
        self.hand = Hand()



class Table :
    def __init__(self, dealer):
        self.deck = TableDeck()
        self.players = []
        self.dealer = dealer

    def add_player(self, player):
        self.players.append(player)





class Dealer :
    def __init__(self):
        self.deck = DealerDeck()






new_deck = Deck()


#print(new_deck)
#new_deck.shuffle_cards()
#print(new_deck)

#new_deck.sort_cards_by_color()
#new_deck.sort_cards_by_number()



card = Card(3, 'SPADES')

#new_deck.remove_card(card)

#new_deck.remove_card(card)


#new_deck.add_card(card)

#print(len(new_deck))


new_hand = Hand()

print(len(new_hand))

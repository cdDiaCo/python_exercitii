
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
        print("in remove")
        if card in self:
            self.remove(card)
        else:
            print("Card cannot be removed. Card not present in deck")



class HandDeck(Deck):

    def add_card(self, card):
        if len(self) >= 2 :
            print("HandDeck can have max. two cards")
        else :
            super(HandDeck, self).add_card(card)



class DealerDeck(Deck):
    colors = ["SPADES", "HEARTS", "DIAMONDS", "CLUBS"]

    def __init__(self):
        Deck.__init__(self)

        for color in self.colors:
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



    def sort_cards(self, card):
        self.sort(key=lambda card: (card.card_color, card.card_number))





class TableDeck(Deck):

    def add_card(self, card):
        if len(self) >= 5 :
            print("TableDeck can have max. five cards")
        else :
            super(TableDeck, self).add_card(card)



class Card() :

    def __init__(self, card_number, card_color):
        self.card_number = card_number
        self.card_color = card_color

    def __eq__(self, other):
        if self.card_number == other.card_number and self.card_color == other.card_color :
            return True
        return False


    def get_card_color(self):
        return self.card_color


    def get_card_number(self):
        return self.card_number


    def __str__(self):
        return self.get_card_color() + " " + str(self.get_card_number())



class Player :

    def __init__(self):
        self.deck = HandDeck()


    def add_card(self, card):
        self.deck.add_card(card)


    def remove_card(self, card):
        self.deck.remove_card(card)



class Table :
    def __init__(self, dealer):
        self.deck = TableDeck()
        self.players = []
        self.dealer = dealer

    def add_player(self, player):
        self.players.append(player)


    def add_card(self, card):
        self.deck.add_card(card)

    def remove_card(self, card):
        self.deck.remove_card(card)





class Dealer :
    def __init__(self):
        self.deck = DealerDeck()


    def sort_cards(self, card):
        self.deck.sort_cards(card)


    def shuffle_cards(self):
        self.deck.shuffle_cards()


    def add_card(self, card):
        self.deck.add_card(card)


    def remove_card(self, card):
        self.deck.remove_card(card)


    def deal_card(self, receiver):
        card = self.deck.pop()
        receiver.deck.add_card(card)





def print_cards(deck):
    for elem in deck:
        print(elem.__str__())



new_dealer = Dealer()
new_table = Table(new_dealer)


player_one = Player()
player_two = Player()


new_table.add_player(player_one)
new_table.add_player(player_two)


card_one = Card(15, "SPADES")
#card_two = Card(15, "HEARTS")
#card_three = Card(15, "DIAMONDS")


new_dealer.shuffle_cards()
new_dealer.sort_cards(card_one)


new_dealer.deal_card(player_two)
new_dealer.deal_card(player_two)



new_dealer.deal_card(new_table)
new_dealer.deal_card(new_table)


#----------------




#card_one = Card(15, "SPADES")
#card_two = Card(15, "HEARTS")
#card_three = Card(15, "DIAMONDS")




#new_dealer.sort_cards_by_color(card_one)
#new_dealer.sort_cards_by_number(card_one)


#new_dealer.remove_card(card_one)
#new_dealer.remove_card(card_two)
#new_dealer.remove_card(card_three)


#new_dealer.remove_card(card_one)




#player_two.add_card(card_one)
#player_two.add_card(card_two)
#player_two.remove_card(card_two)


#new_table.add_card(card_three)
#new_table.add_card(card_two)
#new_table.remove_card(card_three)







print_cards(new_dealer.deck)


print("-----------------------")

print_cards(player_two.deck)


print("----------------")

print_cards(new_table.deck)
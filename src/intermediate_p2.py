

# TODO when cards are dealt, remove them from dealerDeck, and add them to the other decks
# TODO add new methods for some classes to avoid a 'long chain of calls'
# TODO try to change the sort methods


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
    def __init__(self):
        Deck.__init__(self)


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



    def sort_cards_by_number(self):
        num_of_sorted_cards = 0
        for num in range(2, 16):
            if num == 11:
                continue

            for i in range(num_of_sorted_cards, len(self)):

                if self[i].get_card_number() == num :
                    continue
                else:
                    for j in range(i+1, len(self)):

                        if self[j].get_card_number() == num :
                            temp = self[i]
                            self[i] = self[j]
                            self[j] = temp

                            break
            num_of_sorted_cards += 4



    def sort_cards_by_color(self, card):
        def sortFirst(val):
            return card.get_card_color()

        self.sort(key=sortFirst)


'''
    def sort_cards_by_color(self):
        num_of_sorted_cards = 0
        for color in self.colors:
            for i in range(num_of_sorted_cards, len(self)) :

                if self[i].get_card_color() == color:
                    continue
                else:
                    for j in range(i+1, len(self)):
                        if self[j].get_card_color() == color:
                            temp = self[i]
                            self[i] = self[j]
                            self[j] = temp

                            break
            num_of_sorted_cards += 13
'''




class TableDeck(Deck):
    def __init__(self):
        Deck.__init__(self)


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


    def get_card_description(self):
        description = self.get_card_color() + " " + str(self.get_card_number())
        return  description



'''
class Hand() :
    def __init__(self):
        self.hand_deck = HandDeck()
'''


class Player :
    def __init__(self):
        self.hand = HandDeck()



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




def print_cards(deck):
    for elem in deck:
        print(elem.get_card_description())



new_dealer = Dealer()
new_table = Table(new_dealer)


player_one = Player()
player_two = Player()


new_table.add_player(player_one)
new_table.add_player(player_two)




dealer_deck = DealerDeck()
dealer_deck.shuffle_cards()


card_one = Card(15, "SPADES")



dealer_deck.sort_cards_by_color(card_one)
#dealer_deck.sort_cards_by_number()



#card_two = Card(15, "HEARTS")
#card_three = Card(15, "DIAMONDS")
#dealer_deck.remove_card(card_one)
#dealer_deck.remove_card(card_two)
#dealer_deck.remove_card(card_three)

#dealer_deck.add_card(card_one)




#player_two.hand.add_card(card_one)
#player_two.hand.add_card(card_two)


#new_table.deck.add_card(card_three)
#new_table.deck.remove_card(card_three)


#print(new_table.deck)

#print(new_card.get_card_description())


print_cards(dealer_deck)







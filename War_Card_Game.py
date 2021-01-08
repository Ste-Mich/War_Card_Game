# SUIT,RANK,VALUE
import random
suits = ("Hearths", "Diamonds", "Spades", "Clubs")
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card():

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck():

    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def show_cards(self):
        for card in self.all_cards:
            print(card)

    def shuffle_cards(self):
        random.shuffle(self.all_cards)
        print("Karty zamíchány")

    def deal_one(self):
        return self.all_cards.pop()


class Player():

    def __init__(self, name):

        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f"player {self.name} has {len(self.all_cards)} cards"


player1 = Player(input("Choose the name of Player 1:"))
player2 = Player(input("Choose the name of Player 2:"))
the_deck = Deck()
the_deck.shuffle_cards()

for _ in range(26):
    player1.add_cards(the_deck.deal_one())
    player2.add_cards(the_deck.deal_one())

game_on = True
round_num = 0

while game_on:

    round_num += 1
    print("Round starts {}".format(round_num))
    print(f"{player1.name} has {len(player1.all_cards)} cards. {player2.name} has {len(player2.all_cards)} cards.")

    if len(player1.all_cards) == 0:
        print(f"Vyhrál {player2.name}")
        game_on = False
        break
    if len(player2.all_cards) == 0:
        print(f"Vyhrál {player1.name}")
        game_on = False
        break

    player_one_cards = []
    player_two_cards = []
    player_one_cards.append(player1.remove_one())
    player_two_cards.append(player2.remove_one())

    war_on = True

    while war_on:

        if player_one_cards[-1].value > player_two_cards[-1].value:
            player1.add_cards(player_one_cards)
            player1.add_cards(player_two_cards)
            war_on = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player2.add_cards(player_one_cards)
            player2.add_cards(player_two_cards)
            war_on = False

        else:
            print("WAR!!!")

            if len(player1.all_cards) < 5:
                print(f"{player1.name} does not have enough cards to start a war...")
                print(f"{player2.name} WON.")
                game_on = False
                break

            elif len(player2.all_cards) < 5:
                print(f"{player2.name} does not have enough cards to start a war...")
                print(f"{player1.name} WON.")
                game_on = False
                break

            else:
                for num in range(5):
                    player_one_cards.append(player1.remove_one())
                    player_two_cards.append(player2.remove_one())

input("Press any key to exit...")

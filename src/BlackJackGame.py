import random
from tkinter import *
from tkinter import ttk

class Card:
    """Card class, has suit & value."""
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.suit} of {self.value}"

class Deck:
    """"Responsible for making the deck randomly. Should provide 52"""
    def __init__(self):
        suits = ['hjerte', 'spar', 'ruder', 'klør']
        self.cards = [Card(suit = suit, value = value) for value in range(1, 14) for suit in suits]
        random.shuffle(self.cards)
    def deal_card(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def show_dealers_first_card(self):
        return self.cards[0]
    
    def calculate_value(self):
        value = 0
        aces = 0

        for card in self.cards:
            if card.value in [11, 12, 13]:
                value += 10
            elif card.value == "1":
                aces += 1
            else:
                value += int(card.value)
        for _ in range(aces):
            if value + 11 <= 21:
                value += 11
            else:
                value += 1
        
        return value
            
class Bet:
    def __init__(self):
        self.value = self.initial_bet()
    
    def initial_bet(self):
        
        player_bet = int(input("Please place starting bet now."))
        if player_bet <= 0:
            print("INvalid bet, please bet some money")
        return player_bet
    
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return int(self.value)
        
        
class BlackJack():
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.player_current_bet = Bet() 

        self.dealer_hand = Hand()
        
    def initial_deal(self):
        for _ in range(2):
            self.player_hand.add_card(self.deck.deal_card())
            self.dealer_hand.add_card(self.deck.deal_card())
    
    def print_player_current_state(self):
        print( "your hand value:", self.player_hand.calculate_value(),
            "Dealer card:", self.dealer_hand.show_dealers_first_card(),
            ", your bet:", self.player_current_bet,
            "Your cards:", self.player_hand.cards, 
            )

    def player_hit(self):
        self.player_hand.add_card(self.deck.deal_card())

    def dealer_hit(self):
        self.dealer_hand.add_card(self.deck.deal_card())
    def begin_asking_player_for_moves(self):
        print("Starting game.")
        bet = prompt_player_for_bet()
    # prompt the player for input
    def prompt_player(self):
        print("Please choose to Hit or Stand")
        # print("Your bet:", self.player_current_bet.__str__())
        # print("your cards:", self.player_hand.cards)
        self.print_player_current_state()
        choice = input("please choose now")
        if choice not in ['s', 'S', 'h', 'H']:
            print("Invalid input, please choose Hit or Stay!")
        
        elif choice in ['h', 'H']:
            print("Hitting ...")
            self.player_hand.add_card(self.deck.deal_card())
            self.print_player_current_state()
            if self.player_hand.calculate_value() >= 22:
                print("inside elif of prompt_player, YOU LOST")
                self.print_player_current_state() #tjek at spiller ikke har tabt ved at hitte.
            elif self.player_hand.calculate_value() == 21:
                print("inside prompt_player, player hand == 21, BLAKJACK")
            else:
                self.prompt_player()
            # tjek player value hand imod 21
            # hvis 21 eller over, gå til dealer-vinder-afslutning
            #hvis IKKE over, lad spiller blive i input loop,
        elif choice in ['s', 'S']:
            print("standing")
            self.print_player_current_state()
            self.start_dealer_turn()
        
    def start_dealer_turn(self):
        print("starting dealers turn")
        while self.dealer_hand.calculate_value() < 17:
            print("inside start dealer turn of while")
            self.dealer_hand.add_card(self.deck.deal_card())
            print("dealer val:", self.dealer_hand.calculate_value())
        print("dealers cards:", self.dealer_hand.cards)
        print("dealer value:", self.dealer_hand.calculate_value())
        print(self.determine_winner())    
        # if self.dealer_hand.calculate_value() >= 22:
        #     print("dealer lost, hand above 22", self.dealer_hand.calculate_value())
        # elif self.dealer_hand.calculate_value() == 21:
        #     print("dealer has blackjack")


    def determine_winner(self):
        print("inside determiner winner")
        player_value = self.player_hand.calculate_value()
        dealer_value = self.dealer_hand.calculate_value()

        if player_value > 21:
            return "Dealer Wins (Player Bust)"
        elif dealer_value > 21:
            return "Player Wins (Dealer Bust)"
        elif player_value > dealer_value:
            return "Player Wins"
        elif player_value < dealer_value:
            return "Dealer Wins"
        else:
            return "It's a tie!"


class Gui:
    def __init__(self, root):
        self.root = root
        self.game = BlackJack()

        #setup
        self.root.title("Blackjack")
        self.label = 

if __name__ == "__main__":
    #what i realy need here is a class that is agui which clals the other tihngs
    #right here

    game = BlackJack()
    game.initial_deal()
    #should have a function here that starts the game asking itself
    game.prompt_player()#this call to prompt should be at the end.
    root = Tk()
    Gui(root)

root.mainloop()

#trey creating a butto here that just does some things.

# start game 
# shuffle deck 
# player bets 
# deal cards -- spiller får to 
# dealer for 1 synligt og et usynligt kort
# vil sppiller stå eller gå?
# indtil spiller står eller er >21, tjek igen
#
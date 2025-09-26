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
    """Takes a number of cards, & calculates their Blackjack value."""
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
    """Has the amount of money a player has bet."""
    def __init__(self):
        self.value = self.initial_bet()
    
    def initial_bet(self):
        
        player_bet = int(input("Please place your bet now, sum from 1 and up."))
        if player_bet <= 0:
            print("Invalid bet, please bet some money")
        return player_bet
    
    def __str__(self):
        return str(self.value)
    def __repr__(self):
        return int(self.value)
        
        
class BlackJack():
    """Game execution class, calls bets, decks and player."""
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
    def prompt_player(self):
        print("Please choose to Hit or Stand (use 'h' for hit and 's' for stand).")
        self.print_player_current_state()
        choice = input("please choose now")
        if choice not in ['s', 'S', 'h', 'H']:
            print("Invalid input, please choose Hit or Stand!")
        
        elif choice in ['h', 'H']:
            print("Hitting ...")
            self.player_hand.add_card(self.deck.deal_card())
            if self.player_hand.calculate_value() >= 22:
                print("Your hand value is", self.player_hand.calculate_value(), ", that's more than 21!")
                print(self.determine_winner())
            elif self.player_hand.calculate_value() == 21:
                print("Your hand value is 21, that's a BLAKJACK! No better hand possible, automatic stand.")
            else:
                self.prompt_player()
        elif choice in ['s', 'S']:
            print("Player chose to stand.")
            self.print_player_current_state()
            self.start_dealer_turn()
        
    def start_dealer_turn(self):
        print("Starting dealer's turn")
        while self.dealer_hand.calculate_value() < 17:
            print("Dealer hitting card ...")
            self.dealer_hand.add_card(self.deck.deal_card())
        print(self.determine_winner())    


    def determine_winner(self):
        print("Determining winner by hand value ...")
        player_value = self.player_hand.calculate_value()
        dealer_value = self.dealer_hand.calculate_value()

        print("Dealer's final hand:", self.dealer_hand.cards)
        print("Dealer's hand's value:", self.dealer_hand.calculate_value())
        print("Player's final hand:", self.player_hand.cards)
        print("Player's hand's value:", self.player_hand.calculate_value())

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

if __name__ == "__main__":
    game = BlackJack()
    game.initial_deal()
    game.prompt_player()
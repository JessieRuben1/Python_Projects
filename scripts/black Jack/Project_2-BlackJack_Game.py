#Black Jack Textual game
import random

# A tuple of suits
suits = ("Hearts", "Clubs", "Diamonds", "Spades")

# A tuple of ranks
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", 
         "Ten", "Jack", "Queen", "King", "Ace")

# A dictionary that contains the values of the cards.
values = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,
          "Ten":10,"Jack":10,"Queen":10,"King":10,"Ace":11}

# The Card class takes in two arguments, suit and rank, and assigns them to the object's suit and rank
# attributes
class Card:
    def __init__(self, suit, rank):
        """
        This function takes in two arguments, suit and rank, and assigns them to the object's suit and
        rank attributes.
        
        :param suit: The suit of the card
        :param rank: 1-13
        """
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        """
        The __str__() function returns a string representation of the object
        :return: The rank and suit of the card.
        """
        return f"{self.rank} of {self.suit}"
    
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append((suit,rank))
    
    def shuffle(self):
        """
        The function shuffle() takes a deck of cards and shuffles it
        """
        random.shuffle(self.deck)
        
    def deal(self):
        """
        It takes the last card from the deck and returns it.
        :return: The take_cards variable is being returned.
        """
        take_cards = self.deck.pop()
        return take_cards


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.ace = 0
    
    def add_cards(self, card):
        self.cards.append(card)
        self.value += values[card[1]]
        
    
    def adjust_for_ace(self):
        if self.cards[0][1] == "Ace" or self.cards[1][1] == "Ace":
            if self.value < 11:
                values["Ace"] = 11
            elif self.value > 10:
                values["Ace"] = 1

class Chips:
    def __init__(self):
        self.total = 300
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet
    
    def push(self):
        self.total = self.total
        

def take_bet(C):
    C.bet = int(input("Enter your bet: "))
    if C.total == 0 and C.bet > C.total:
        raise Exception("You got zero money lef. You lose")
    while C.bet >C.total or C.bet < 0 or not (isinstance(C.bet, int)):
        C.bet = int(input("Enter your bet: "))
        
def hit(D, hand):
    hand.add_cards(D.deal())
    hand.adjust_for_ace()
    
def hit_or_stand(D, hand):
    while True:
        hit_stand = input("Do you want to hit or stand? ").lower()
        if hit_stand == "hit" or hit_stand == "h":
            hit(D,hand)
        else:
            print("PLAYER STAND, DEALER IS PLAYING")
            return False
        return True
    

def show_some(player_hand, dealer_hand):
    print("PLAYER cards: ", player_hand.cards)
    print("DEALER CARDS: ", dealer_hand.cards)


def show_all(player_hand, dealer_hand):
    print("PLAYER cards : ", player_hand.cards)
    #print(player_hand.cards)
    print("DEALER cards : ", dealer_hand.cards)
    #print(dealer_hand.cards)

def player_busts(C, player_hand, dealer_hand):
    C.lose_bet()
    print("*** PLAYER BUST ***")
    
def player_wins(C, player_hand, dealer_hand):
    C.win_bet()
    print("*** PLAYER WINS ***")
    
def dealer_busts(C, player_hand, dealer_hand):
    C.win_bet()
    print("*** DEALER BUST ***")
    

def dealer_wins(C, player_hand, dealer_hand):
    C.lose_bet()
    print("*** DEALER WINS ***")
    
def push(C, player_hand, dealer_hand):
    print("PUSH")
    C.push()
                

def play_again():
    return input("Do you want to play again? ").lower().startswith("y")


def main():
    win = 0
    lose = 0
    tie = 0
    
    print("*****WELCOME TO BLACKJACK*****")
    print(
        "INSTRUCTION: 1)Bet should be lower than your total money or equal to it (300 is the current)"
    )
    print("2)Answer with y/n OR yes/no when you want to play another hand")
    print("3)answer with  H/S OR hit/stand  to hit or stand")
    
    C = Chips()
    while True:
        D = Deck()
        D.shuffle()
        player_hand = Hand()
        dealer_hand = Hand()
        
        player_hand.add_cards(D.deal())
        player_hand.add_cards(D.deal())
        dealer_hand.add_cards(D.deal())
        dealer_hand.add_cards(D.deal())
        
        take_bet(C)
        show_some(player_hand,dealer_hand)
        while hit_or_stand(D, player_hand):
            show_some(player_hand, dealer_hand)
            if player_hand.value > 21:
                show_all(player_hand,dealer_hand)
                player_busts(C, player_hand, dealer_hand)
                lose += 1
                print(f"Wins = {win},Loses = {lose}, Tie = {tie}")
                break
        if player_hand.value <=21:
            while dealer_hand.value < 17:
                hit(D, dealer_hand)
            show_all(player_hand, dealer_hand)
            if dealer_hand.value > 21:
                dealer_busts(C, player_hand, dealer_hand)
                win += 1
                print(f"Wins  =  {win},Loses =  {lose}, Tie  =  {tie}")
            elif dealer_hand.value > player_hand.value:
                dealer_wins(C, player_hand, dealer_hand)
                lose += 1
                print(f"Wins  =  {win},Loses =  {lose}, Tie  =  {tie}")
            elif dealer_hand.value < player_hand.value:
                player_wins(C, player_hand, dealer_hand)
                win += 1
                print(f"Wins  =  {win},Loses =  {lose}, Tie  =  {tie}")
            else:
                push(C, player_hand, dealer_hand)
                tie += 1
                print(f"Wins  =  {win},Loses =  {lose}, Tie  =  {tie}")
      
        print(f"Your Total money ={C.total}")
        if play_again():
            continue
        else:
            print("Thanks for playing")
            print(
                f"Number of Wins  =  {win},Number of Loses =  {lose}, Number of Tie  =  {tie}"
            )
            break
                
        
if __name__ == '__main__':
    main()       
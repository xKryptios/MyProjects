import random

#setup deck , cards and hand calss
suits = ("Spade","Hearts","Diamond","Clubs")
ranks = ("2","3","4","5","6","7","8","9","10","J","Q","K","Ace")
values = {"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"10":10,"J":10,"Q":10,"K":10,"Ace":11}
class Card:
    def __init__(self,rank,suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return self.rank + " of " + self.suit

class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(rank,suit))

    def __str__(self):
        deck_comp = 'The deck contains :\n'
        for item in self.deck:
            deck_comp += item.__str__() + '\n'
        return deck_comp

    def draw_card(self):
        card = self.deck.pop()
        return card

class Hand:
    def __init__(self):
        self.cards = []
        
    def add_card(self,Card):
        self.cards.append(Card)

    def __str__(self):
        hand_comp = ''
        for item in self.cards:
            hand_comp += item.__str__() + '\n'
        return hand_comp

    def aces(self):
        ace = 0
        for card in self.cards:
            if card.rank == "Ace":
                ace += 1
        return ace

    def value(self):
        value = 0
        for card in self.cards:
            value += values[card.rank]
        #make adjustment for value due to A
        ace_counter = self.aces()
        while value>21 and ace_counter>0:
            value -= 10
            ace_counter -=1
        return value

class Chips:
    def __init__(self):
        self.total = 500
    def __str__(self):
        return 'Your balance: $' + str(self.total)

    def lose(self,bet):
        self.total -= bet
        print(f"You Lost ${bet}!")
    def win(self,bet):
        self.total += bet
        print(f"You Won ${bet}!")

def ask_bet(playerchips):
    '''
    ask user for bet(int only) parse total player chips
    return ammount of chip user inputted
    '''
    bet = 0
    while not (bet<=playerchips and bet> 0):
        while True:
            try:
                bet = int(input('Enter your bet: '))
            except ValueError:
                continue
            else:
                break
    return bet

def hit_or_stand():
    hit_stand = ''
    while not(hit_stand == "hit" or hit_stand == 'stand'):
        hit_stand = input("Enter hit or stand: ")
    return hit_stand


#excution of game and initialise chips
player_chip = Chips()

while True:

    #prep for each round
    while True:
        #initialise player and deck , show balance 
        new_deck = Deck()
        dealer_hand = Hand()
        player_hand = Hand()
        print(f"Your total balace: {player_chip.total}")

        #ask for chip to bet, verify if is integer and within budget
        bet_chip = ask_bet(player_chip.total)
        
        random.shuffle(new_deck.deck)
        print("deck is shuffled")

        #player and dealer each take turn to draw 1 card 2times
        print("drawing cards...")
        card1 = new_deck.draw_card()
        player_hand.add_card(card1)
        card2 = new_deck.draw_card()
        dealer_hand.add_card(card2)
        card3 = new_deck.draw_card()
        player_hand.add_card(card3)
        card4 = new_deck.draw_card()
        dealer_hand.add_card(card4)

        #display dealer and player cards drawn
        print(f"Dealer's hand: {card2}, ? ")
        print("player hand:\n"+player_hand.__str__())
        print(f"\nValue in hand: {player_hand.value()}")

        #check for blackjack or AA
        if player_hand.value == 21 or (card1.rank == 'ace' and card3.rank == 'ace'):
            print("Blackjack! You win!")
            player_chip.win(bet_chip)
            break
            
        #ask for player decision, only break out of loop if player choose stand or card==5
        while True:
            if len(player_hand.cards)==5:
                break
            player_decision = hit_or_stand()
            if player_decision == 'stand':
                break

            #draw 3rd to 5th cards
            player_hand.add_card(new_deck.draw_card())
            print("\n"*100)
            print(f"Dealer's hand: {card2}, ? ")
            print(f"Number of cards in hand:\n{player_hand}")
            print(f"Value in hand: {player_hand.value()}")
            print(f"No. Cards: {len(player_hand.cards)}")

            if player_hand.value()>=21:
                break
    
        #if player bust or hit blackjack
        if player_hand.value()>21:
            player_chip.lose(bet_chip)
            break
        elif player_hand.value()==21:
            player_chip.win(bet_chip)
            break

        #dealer's turn to draw
        while True:
            if player_hand.value()>dealer_hand.value() and dealer_hand.value()<17:
                dealer_hand.add_card(new_deck.draw_card())
                print("\n"*100)
                print(f"Dealer's cards: \n{dealer_hand}")
                print(f"Player's cards:\n{player_hand}")
                print(f"Player's hand value: {player_hand.value()}")
                print(f"Dealer's hand value: {dealer_hand.value()}")
                print(f"No. Cards: {len(player_hand.cards)}")
                
            else:
                print("\n"*100)
                print(f"Dealer's cards: \n{dealer_hand}")
                print(f"Player's cards:\n{player_hand}")
                print(f"Player's hand value: {player_hand.value()}")
                print(f"Dealer's hand value: {dealer_hand.value()}")
                print(f"No. Cards: {len(player_hand.cards)}")
                break

        #dealer bust
        if dealer_hand.value()>21:
            player_chip.win(bet_chip)
            break

        #if dealer less than player and dealer 17<x<21
        elif player_hand.value()>dealer_hand.value():
            player_chip.win(bet_chip)
            break
        #if dealer more than player
        elif player_hand.value()<dealer_hand.value():
            player_chip.lose(bet_chip)

        else:
            print("its a draw")
            break
        


    #ask for another round
    if player_chip.total<=0:
        print("you have no balance left to play")
        print("you suck haha")
        break
    replay = ''
    while not ( replay == "Y" or replay == "N"):
        replay = input("another round? Y/N ").upper()
    
    if replay == "N":
        break
    else:
        continue

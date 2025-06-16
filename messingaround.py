from random import choice, randint


class DeckOfCards():

    def __init__(self):
        self.full_deck = self.new_deck()
        self.color = {"Red": ['♦️', '♥️'], "Black": ['♣️', '♠️']}

    def new_deck(self):
        suits = ['♣️', '♠️', '♦️', '♥️']
        deck = [Card(num, suit) for num in range(2, 15) for suit in suits]
        return deck

class Card:
    face_cards = {11: 'J', 12: 'Q', 13: 'K', 14: 'A'}

    def __init__(self, num, suit):
        self.num = num
        self.suit = suit

    def __str__(self):
        if self.num in self.face_cards:
            return f'{self.face_cards[self.num]}{self.suit}'
        else:
            return f'{self.num}{self.suit}'
    
    def __repr__(self):
        if self.num in self.face_cards:
            return f'{self.face_cards[self.num]}{self.suit}'
        else:
            return f'{self.num}{self.suit}'
            
class Player():
    def __init__(self,deck):
        self.deck = deck
        self.pile = self.deal()
        self.points = 0
    
    def deal(self):
        pile = []
        for i in range(26):
            card = self.deck.full_deck.pop(randint(0,len(self.deck.full_deck)-1))
            pile.append(card)
        return pile
    
    def draw_four(self):
        self.hand = []
        for i in range(4):
            card = self.pile.pop(0)
            self.hand.append(card)
    
    def cpu_pick_card(self):
        self.draw_four()
        return self.hand[randint(0,3)]
    
class User(Player):
    def __init__(self,deck):
        super().__init__(deck)

    def pick_card_input(self):
  
        while True:
            card = int(input("Pick a card: "))-1
            if 0 <= card <= 3:
                break
            else:
                print("pick a card 1-4")
        return card
    
    def pick_card(self):
        self.draw_four()
        self.show_hand(self.hand)
        card = self.pick_card_input()
        self.card = self.hand[card]
        return self.card
    
    def show_hand(self,hand):
        for i in range(len(hand)):
            print(f"{hand[i]} ",end="")
        print()


class Game(DeckOfCards):

    def __init__(self,player,cpu):
        super().__init__()
        self.player = player
        self.cpu = cpu

    def turn(self):
        player_card = self.player.pick_card()
        cpu_card = self.cpu.cpu_pick_card()
        if (cpu_card.suit in self.color["Red"] and player_card.suit in self.color["Red"]) or (cpu_card.suit in self.color["Black"] and player_card.suit in self.color["Black"]):
            self.same(player_card,cpu_card)
        else:
            self.different(player_card,cpu_card)

    def same(self,player_card,cpu_card):
        print(f"{player_card} V.S {cpu_card}")
        if player_card.num != cpu_card.num:
            if player_card.num < cpu_card.num:
                print("You Win")
                self.player.points += 1
            else:
                print("You Lose")
                self.cpu.points += 1
        else:
            print("Its a Tie")
        print(f"player: {self.player.points}\ncpu: {self.cpu.points}")

    def different(self,player_card,cpu_card):
        print(f"{player_card} V.S {cpu_card}")
        if player_card.num != cpu_card.num:
            if player_card.num > cpu_card.num:
                print("You Win")
                self.player.points += 1
            else:
                print("You Lose")
                self.cpu.points += 1
        else:
            print("Its a tie")
        print(f"player: {self.player.points}\ncpu: {self.cpu.points}")
        

deck = DeckOfCards()
player = User(deck)
cpu = Player(deck)
game = Game(player,cpu)
for i in range(4):
    game.turn()





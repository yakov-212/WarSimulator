import random
class Card:

    def __init__(self,num,suit):
        self.num = num
        self.suit = suit

    def __str__(self):
        face = ["Jack","Queen","King","Ace"]
        num = self.num
        if self.num > 10:
            num = face[self.num-11]
        return f"{num} of {self.suit}"
    
class Deck:

    def __init__(self):
        self.cards = []
        self.make_deck()
        self.cards = self.shuffle(self.cards)

    # left some code that i worked on before realizing I needed all the numbers as ints for game logic
    def make_deck(self):
        suit = ["Diamonds", "Hearts", "Spades","Clubs"]
        for i in range(52):
            self.cards.append(Card((int(i/4))+2,suit[int(i%4)]))
            # else:
            #     self.cards.append(Card(face[int(i/4)-9],suit[int(i%4)]))

    def get_card(self,cards):
        num = len(cards)
        rand = random.randint(0,num)-1
        if num > 0:
            return cards.pop(rand)
        else:
            return False
        
    # Takes cards as a paramater so it could  be use to shuffle playes pile
    # It used to not return anything as well   
    def shuffle(self,cards):
        temp = []
        while(True):
            c = self.get_card(cards)
            if c:
                temp.append(c)
            else:
                cards = temp
                return cards
            
    def print_cards(self):
        for i in range(len(self.cards)):
            print(self.cards[i])
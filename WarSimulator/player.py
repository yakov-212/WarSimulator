class Player:
    def __init__(self,deck,name):
        self.name = name
        self.deck = deck
        self.players_deck = []
        self.hand = []
        self.pile = []
        self.war_wins = 0

    def take_from_deck(self):
        c = self.deck.get_card(self.deck.cards)
        if c:
            self.players_deck.append(c)
            
    def pick_card(self):
        card = False
        if self.pile and not self.players_deck:
            self.players_deck = self.deck.shuffle(self.pile)
        if self.players_deck:
            card = self.players_deck.pop(0)
            self.hand.append(card)
        return card
    
    def war(self):
        #print(f"{self.name} war cards")
        for i in range(3):
            if not self.pick_card():
                return
            #print(self.hand[-1])

    def print_hand(self):
        for i in range(len(self.hand)):
            print(self.hand[i])

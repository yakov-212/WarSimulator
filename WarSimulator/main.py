from deck import Deck
from player import Player

d = Deck()
p1 = Player(d,"Player One")
p2 = Player(d,"Player Two")

# uncomment print statements inside Player.war() method for more clarity
def fight():
        #print(f"{p1.hand[-1]} V.S {p2.hand[-1]}")
        global war_amount
        global war
        if p1.hand[-1].num > p2.hand[-1].num:
            winner = p1
            loser = p2
        elif p1.hand[-1].num < p2.hand[-1].num:
            winner = p2
            loser = p1
        else:
            war = True
            p1.war()
            p2.war()
            return fight()
        if war:
            winner.war_wins += 1
            war_amount += 1
        return winner,loser

for i in range(26):
    p1.take_from_deck()
    p2.take_from_deck()
round = 0
war_amount = 0
while (p1.players_deck and p2.players_deck):
    round += 1
    war = False
    p1.hand = []
    p2.hand = []
    p1.pick_card()
    p2.pick_card()

    winner,loser = fight()
    for i in range(len(winner.hand)):
        winner.players_deck.append(winner.hand[i])

    for i in range(len(loser.hand)):
        winner.players_deck.append(loser.hand[i])

print(f"{winner.name} Won!!! \nIt took {round} rounds \nThere were {war_amount} wars")
print(f"{p1.name} Won {p1.war_wins} Wars \n{p2.name} Won {p2.war_wins} Wars")
if winner.war_wins < loser.war_wins:
    print("Achivment Unlocked! \nWhat Luck")
elif winner.war_wins == loser.war_wins:
    print("Achivment Unlocked! \nBy The Skin Of Your Teeth")

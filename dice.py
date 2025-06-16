import time
import random

times_rolled = 0
stop = 0

class Dice:
    def __init__(self):
        self.amount = random.randint(1, 6)

while True:
    try:
        amount = int(input("How many dice do you want to roll 1-99? "))
    except ValueError:
           print("Type only numbers please")
           continue
    if 100 > amount > 0:
        break
    else:
        print("only nunbers 1-99 are accapted")
start = time.time()  
      
while stop < amount:
    rolls = [Dice() for i in range(amount)]
    times_rolled += 1
    for roll in rolls:
        print(roll.amount, end=' ')
    print()
    for roll in rolls:
        if roll.amount == rolls[0].amount:
            stop += 1
        else:
            stop = 0


end = time.time()

print(f"you rolled {times_rolled} Times\n"
      f"And Took {round(end - start, 2)} seconds")

import random as r
import copy
import os

clear = lambda: os.system("cls")


class Board:
    def __init__(self):
        self.board = []
        for i in range(4):
            self.board.append([0,0,0,0])
    
    def __str__(self):
        return f"{self.board[0]}\n{self.board[1]}\n{self.board[2]}\n{self.board[3]}"
            
    def add_rand(self):
        while True:
            i,j,n = r.randint(0,3),r.randint(0,3),r.choice([2,4,2,2])
            if self.board[i][j] == 0:
                self.board[i][j] = n
                break
    def reset_board(self):
        self.board = []
        for i in range(4):
            self.board.append([0,0,0,0])


class Movments(Board):
    def __init__(self):
        super().__init__()

    def right_left(self,direct):
        for index in range(4):
            n = self.board[index].count(0)
            for i in range(n):
                self.board[index].remove(0)
            for i in range(n):
                if direct == "d" or direct == "s":
                    self.board[index].insert(i,0)
                else:
                    self.board[index].append(0)

    def vertical(self,board):
                b = [[],[],[],[]]
                for index in range(4):
                    for i in range(4):
                        b[index].append(board[i][index])
                board = b
                return board

    def up_down(self,direct):
        self.board = self.vertical(self.board)
        self.right_left(direct)
        self.board = self.vertical(self.board)
        

class AddiMoves(Movments):   
    def __init__(self):
        super().__init__()     
    
    def add(self,direct):
        done = True
        if direct == "d":
            for j in range(4):
                for i in range(3):
                    if self.board[j][i] == self.board[j][i+1] and self.board[j][i] != 0:
                        self.board[j][i+1] += self.board[j][i]
                        self.board[j][i] = 0
                        done = False
        elif direct == "a":
            for j in range(4):
                for i in [3,2,1]:
                    if self.board[j][i] == self.board[j][i-1] and self.board[j][i] != 0:
                        self.board[j][i-1] += self.board[j][i]
                        self.board[j][i] = 0
                        done = False
        elif direct == "s":
            for j in range(4):
                for i in [3,2,1,]:
                    if self.board[i][j] == self.board[i-1][j] and self.board[i][j] != 0:
                        self.board[i-1][j] += self.board[i][j]
                        self.board[i][j] = 0
                        done = False
        elif direct == "w":
            for j in range(4):
                for i in range(3):
                    if self.board[i][j] == self.board[i+1][j] and self.board[i][j] != 0:
                        self.board[i+1][j] += self.board[i][j]
                        self.board[i][j] = 0
                        done = False
        return done


class GetMoves(AddiMoves):
    def __init__(self):
        super().__init__()
        
    def turn(self):
        # no one i've ever shown code to has ever known to hit the enter button for inputs
        x = input("ENTER --> ")
        x = x.lower()
        done = False
        accepted = ['a','w','s','d']
        lose = []
        copy_board = copy.deepcopy(self.board)
        attempts = 4
        while not done:
            if x == "d" or x == "a":
                self.right_left(x)
            elif x == "w" or x == "s":
                self.up_down(x)
            done = self.add(x)
            if done:
                if copy_board == self.board:
                    done = False
                    lose.append(x)
                    if "a" in lose and "w" in lose and "s" in lose and "d" in lose:
                        return False
                    clear()
                    print(f"{Board.__str__(self)}")
                    if x in accepted:
                        if lose.count(x) == 1:
                            attempts -= 1
                        print(f"Unable to Move or Merge {attempts} attempts left")
                    else:
                        print("Invalid Response only enter W, A, S, or D")
                    x = input("ENTER --> ")
                    x = x.lower()
            #clears the terminal
            clear()
        return True
    

def greetings():
    clear()
    print("*"*50)
    print("*"*50)
    print(("Welcome to 2048\nTo move the numbers use the W, A, S, or D keys" 
            "\nThe numbers will combine and add together"
            "\nIf you cant combine anything you lose"
            "\nONCE YOU LOSE IN ORDER TO EXIT ENTER EVERY WASD KEY"))
    print("*"*50)
    print("*"*50)
    x = input("Press ENTER to start\nENTER --> ")
    clear()

def main(obj):
    play = True
    play_again = True
    while play_again:
        win = False
        obj.reset_board()
        while play:
            obj.add_rand()
            print(obj)
            play = obj.turn()
            for i in range(4):
                if 2048 in obj.board[i]:
                    win = True
                    print("You win!!! press ENTER to end the game anything else to continue in Survival Mode")
                    play = input("ENTER --> ")


        score = list(map(lambda x: max(x),obj.board))
        score = max(score)     
        if win:
            print("Congrats on winning here's a cookie 🍪")
        print(f"you got a score of {score}!")
        play_again = input("Press ENTER to quit type anything else to play a new game\nENTER --> ")

        

        



    if __name__ == "__main__":
        print("This is all the logic for the 2048 game\n"
            "The should be no reason to run this code...\n"
            "enjoy your easter egg cookies 🍪🍪")



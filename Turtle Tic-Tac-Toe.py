import turtle as turt

screen = turt.Screen()
screen.title("Tic-Tac-Toe")
screen.setup(width=600,height=600)

player = "X"
positions = {}

def check_winner():
    win = False
    win_patterns = [
        [(0,0,), (0,1),(0,2)], #Rows
        [(1,0,), (1,1),(1,2)],
        [(2,0,), (2,1),(2,2)],
        [(0,0,), (1,0),(2,0)], #Columns
        [(0,1,), (1,1),(2,1)],
        [(0,2,), (1,2),(2,2)],
        [(0,0,), (1,1),(2,2)], #Diagnols
        [(0,2,), (1,1),(2,0)],
    ]
    for pattern in win_patterns:
        values = [positions.get(pos) for pos in pattern]
        if len(positions) == 9 and not win:
                display_winner("No One")
                screen.onclick(None)

        if values == ["X","X","X"] or values == ["O","O","O"]:
            win = True
            winner = values[0]
            screen.onclick(None)
            display_winner(winner)



def draw_board():
    board = turt.Turtle()
    board.hideturtle()
    board.speed(0)
    board.pensize(5)

    board.penup()
    board.goto(-300,100)
    board.pendown()
    board.goto(300,100)
    board.penup()
    board.goto(-300,-100)
    board.pendown()
    board.goto(300,-100)

    board.penup()
    board.goto(-100,300)
    board.pendown()
    board.goto(-100,-300)
    board.penup()
    board.goto(100,300)
    board.pendown()
    board.goto(100,-300)


def draw_x(x,y):
    t = turt.Turtle()
    t.speed(0)
    t.hideturtle()
    t.color("red")
    t.pensize(10)

    t.penup()
    t.goto(x - 50,y - 50)
    t.pendown()
    t.goto(x+50,y+50)

    t.penup()
    t.goto(x-50,y+50)
    t.pendown()
    t.goto(x+50,y-50)


def draw_o(x,y):

    t = turt.Turtle()
    t.speed(0)
    t.hideturtle()
    t.color("blue")
    t.pensize(10)

    t.penup()
    t.goto(x,y-40)
    t.pendown()
    t.circle(40)

def convert(col,row):
    if col == 0: x = -200
    elif col == 1: x = 0
    else: x = 200
    if row == 0: y = 200
    elif row ==1: y = 0
    else: y = -200
    return x,y

def display_winner(winner):
    message = turt.Turtle()
    message.hideturtle()
    message.color("green")
    message.penup()
    message.goto(0,-50)
    screen.clear()
    message.write(f"{winner} Wins!", align="center", font=("arial", 50, "bold"))
    

def click_handler(x,y):
    global player
    col = int((x+ 300) // 200)
    row = int((300 - y) // 200)
    x,y = convert(col,row)

    if (col,row) not in positions.keys():
        if player == "X":
            draw_x(x,y)
            positions[(col,row)] = player
            player = "O"
        else:
            draw_o(x,y)
            positions[(col,row)] = player
            player = "X"
        
    check_winner()


draw_board()

screen.onclick(click_handler)
screen.mainloop()
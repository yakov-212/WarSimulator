import turtle
turt = turtle.Turtle()
screen = turtle.Screen()
screen.setup(width=800,height=800)
turt.left(90)
def line(x):
    for i in range(x):
        turt.pendown()
        turt.circle(25,360,6)
        turt.penup()
        turt.forward(45)


turt.penup()
turt.goto(172,-272)
turt.speed(0)
n = 9
turt.left(90)

for i in range(17):
    line(n)
    if i < 8:
        n+=1
    elif i == 8:
        turt.backward(45)
        n-=1
    else:
        turt.backward(45)
        n-=1
    if i%2 == 0:
        turt.right(90)
        turt.backward(12)
        turt.right(90)
        turt.forward(24)
    else:   
        turt.backward(24)
        turt.left(90)
        turt.forward(86)
        turt.left(90)

y1 ,y2,x1,x2= 0,0,0,0
r = 17
ynum = 0
xnum = 0
ynum2 = 0
for i in range(8):
    for i in range(r):
        turt.goto(y1,x1)
        turt.write(f"({x2},{y2})", align="center")
        if i < 8:
            y1+= 45
            y2 +=1
        elif i == 8:
            y1 = ynum -45
            y2 = -1
        else:
            y1-= 45
            y2 -=1
    x2 += 1
    y2 = 0
    ynum -= (20 + ynum2)
    
    y1 = ynum
    x1 += (35 + xnum)

    ynum2+= 2
    xnum += 2
    r -=  1


screen.mainloop()
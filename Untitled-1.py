import time
def pyramid(amount: int, width: int, up_dn: int, rt_lt):
    if up_dn < 0:
        start, stop, j = amount, 0, 0
    else:
        start, stop, j = 0, amount, 1
    if up_dn == rt_lt:
        x = 1
    else:
        x = 0
    for i in range(start,stop,up_dn):
        wmulti = i+j
        print(("1"*wmulti).center(width),flush=True)
        if i%2 == x:
            width = width+2*rt_lt


up, right = 1, 1
down, left = -1, -1
x = y = k = 150
sleep = .15
amount = 20
for i in range(2):
    if i == 0:
        start,stop,step = 1, amount, 1
    else:
        start,stop,step = amount, 1, -1
    for i in range(start,stop,step):
        time.sleep(sleep)
        pyramid(i,k,up,right)
        time.sleep(sleep)
        pyramid(i,x,down,left)
        time.sleep(sleep)
        pyramid(i,k,up,left)
        time.sleep(sleep)
        pyramid(i,y,down,right)
        if i%2 == 0:
            x+=2
        else:
            y-=2




# pyramid(7,40,up,right)
# pyramid(7,46,down,left)
# pyramid(7,40,up,left)
# pyramid(7,34,down,right)


# pyramid(8,40,up,right)
# pyramid(8,46,down,left)
# pyramid(8,40,up,left)
# pyramid(8,32,down,right)


# pyramid(9,40,up,right)
# pyramid(9,48,down,left)
# pyramid(9,40,up,left)
# pyramid(9,32,down,right)

# pyramid(10,40,up,right)
# pyramid(10,48,down,left)
# pyramid(10,40,up,left)
# pyramid(10,30,down,right)

# pyramid(11,40,up,right)
# pyramid(11,50,down,left)
# pyramid(11,40,up,left)
# pyramid(11,30,down,right)




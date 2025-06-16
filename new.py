calc = lambda number, add, number2: number + number2 if add == "+" else (number - number2 if add == "-" and number >= number2 and number >= 0 else "Invalid Operation")


def trans_int(eq):
    z = 0
    for i in range(len(eq)):
        if eq[z] != "+" and eq[z] != "-":
            try:
                eq[z] = int(eq[z])
            except ValueError:
                eq.remove(eq[z])
                z -= 1
        z+= 1
    return eq

while True:
    x = input("Enter equation\n")
    if not x: break

    a = x.split()
    print(a)
    a = trans_int(a)
    print(a)
    if len(a) != 3:
        print("Invalid Input")
        continue

    
    print(calc(a[0],a[1],a[2]))

print(" sdf   sdf sd ".split())

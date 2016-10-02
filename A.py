x = y = 0
while True:
    a = input()
    if a == "Treasure!":
        break
    elif a[0] == "N":
        y += int(a[6:len(a)])
    elif a[0] == "E":
        x += int(a[5:len(a)])
    elif a[0] == "W":
        x -= int(a[5:len(a)])
    elif a[0] == "S":
        y -= int(a[6:len(a)])
print(x, y)
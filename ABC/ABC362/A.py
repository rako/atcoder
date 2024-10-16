intcolor = list(map(int, input().split()))

strcolor = input()

#print(intcolor)

if strcolor == "Red":
    intcolor.pop(0)
elif strcolor == "Green":
    intcolor.pop(1)
elif strcolor == "Blue":
    intcolor.pop(2)

print(min(intcolor))
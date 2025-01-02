n = int(input())
s = input()

flag = 0
for i in s:
    if i == "*":
        if flag == 1:
            print("in")
        else:
            print("out")
    elif i == "|":
        flag += 1
    else:
        continue
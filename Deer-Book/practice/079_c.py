s = input()

a,b,c,d = int(s[0]),int(s[1]),int(s[2]),int(s[3])

total = 0
for i in range(2):
    for j in range(2):
        for k in range(2):
            if i == 0:
                total += a + b
                if j == 0:
                    total += c
                    if k == 0:
                        total += d
                        if total == 7:
                            print(str(a + "+" + b + "+" + c + "+" + d + "=" + 7))
                            exit
                    else:
                        total -= d
                        if total == 7:
                            print(str(a + "+" + b + "+" + c + "-" + d + "=" + 7))
                            exit
                else:
                    total -= c
                    if k == 0:
                        total += d
                        if total == 7:
                            print(str(a + "+" + b + "-" + c + "+" + d + "=" + 7))
                            exit
                    else:
                        total -= d
                        if total == 7:
                            print(str(a + "+" + b + "-" + c + "-" + d + "=" + 7))
                            exit
            else:
                total -= a + b
                if j == 0:
                    total += c
                    if k == 0:
                        total += d
                        if total == 7:
                            print(str(a + "-" + b + "+" + c + "+" + d + "=" + 7))
                            exit
                    else:
                        total -= d
                        if total == 7:
                            print(str(a + "-" + b + "+" + c + "-" + d + "=" + 7))
                            exit
                else:
                    total -= c
                    if k == 0:
                        total += d
                        if total == 7:
                            print(str(a + "-" + b + "-" + c + "+" + d + "=" + 7))
                            exit
                    else:
                        total -= d
                        if total == 7:
                            print(str(a + "-" + b + "-" + c + "-" + d + "=" + 7))
                            exit
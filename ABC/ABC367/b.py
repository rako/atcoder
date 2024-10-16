x = float(input())

strx = str(x)

strx2 = strx.split(".")

xx = strx2[1]

#print(xx)

"""
if int(xx[-1]) == 0:
    if int(xx[1]) == 0:
        ans = int(xx[0]) * 100
    else:
        ans = int(xx[0]) * 100 + int(xx[1]) * 10
else:
    ans = int(xx)
"""

if int(xx) == 0:
    print(int(strx2[0]))
else:
    print(float(float(strx2[0] + "." + xx)))
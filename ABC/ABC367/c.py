n,k = map(int, input().split())

r = list(map(int, input().split()))

rotnum = 0

for i in r:
    rotnum += i

#rlist = [[] * n] * rotnum #全数列の結果格納

r1 = [i-1 for i in r]

rlist2 = []

#rの1~nまでの値文for文を回して、rlistに格納して、条件を確認するだけ
for i in range(n):
    for j in range(i+1, n-1):
        for k in range(r1[j]):
            #rlist[]       


"""
for i in range(n):
if r[i] - 1 >= 1:
diff = r[i] - 1
"""

"""
def rec(n):
    for i in range(n):
        for j in range(1, r[i]+1):
            n * (for k in )
"""

"""
for i in range(n):
    for j in range(r[i]):
        rlist[]
"""

#print(rlist)

"""
if n == 1:
    for a in range(rotnum):
        for b in range(rotnum):
            for c in range(rotnum):
                for d in range(rotnum):
                    for e in range(rotnum):
                        for f in range(rotnum):
                            for g in range(rotnum):
                                for h in range(rotnum):
"""
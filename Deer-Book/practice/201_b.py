n = int(input())

s = []
t = []

for i in range(n):
    iinput = input().split()
    si = str(iinput[0])
    ti = int(iinput[1])
    s.append(si)
    t.append(ti)

#それおれでソートしてインデックスを変数に残してSに持っていく？
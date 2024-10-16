# nut, a, x = [input() for i in range(5)]
# nut = nut.split()
# n = nut[0]
# m = nut[1]
# for i in range(m):
#     total = a[i] + x

# 行の入力
N = list(map(int, input().split())) # Nの中身: [N,M]
N = N[0] # Nの中身: N
M = N[1]

inputMatrix = [] # 行列を格納する配列（この時点では1次元配列）

# 行列の入力
for i in range(N):
   inputVal = list(map(int, input().split()))
   inputMatrix.append(inputVal) # リストの中にリストを格納するので二次元配列となる

total = 0
for i in range(M):
    for j in range(N):
        total += inputMatrix[j,i]
        if total < inputMatrix[0,i]:
            print("No")
        else:
            pass
    #リセット
    total = 0

n,m = map(int, input().split())
graph = [[] for _ in range(n)]

for i in range(m):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b) #一方通行

total = 0
total += n + m #自身と、道の数分一つは動くので
#スタート地点から動けるマスに行くたびにカウントしていき、ゴール地点がスタート地点に被ったときにそこまでの
#経路を合計する
for i in range(n):
    graph[i]
n,m = map(int, input().split())

graph = [[] for _ in range(n)]

for i in range(m):
    a,b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

#再帰関数引数のグラフのリストを呼び出して、その中でさらに関数を呼び出す。
#もし、呼び出すときにカウントが(ループしないので)nになったらルートがある
#もしくは、引数のグラフがないならそこでひとつ前に戻る
def route(n):
    if count2 == n or len(graph[n]) == 0:
        return count2
    count2 = 0
    for xi in graph[n]:
        count2 += 1
        route(xi)

#もし、戻り値がnであるならばルートがあるということでカウントを+1して合計が通り道の数
count = 0
for i in graph[0]:
    if route(i) == n:
        count += 1
print(count)
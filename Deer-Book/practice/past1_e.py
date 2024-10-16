import copy

n,q = map(int, input().split())

graph = [[] for _ in range(n)]

for i in range(q):
    s = list(map(int, input().split()))
    if s[0] == 1:
        a = s[1]
        b = s[2]
        a -= 1
        b -= 1
        graph[a].append(b)
    elif s[0] == 2:
        a = s[1]
        a -= 1
        for i in range(n):
            for j in graph[i]:
                if j == a and i != a:
                    #ここは、graph[i]でj==aの時に、graph[a]にそのiへの辺を付け加える
                    graph[a].append(i)
                    #print(a,i,j)
    elif s[0] == 3: #何が詰まったかというと、for文を回すごとにgraphを書き換えるため新たに参照する値が増えてしまった。
        #解決方法として、deepcopyで元のリストとは別のオブジェクトで元のリストを再生成して参照値が同一に変更されないようにしてから
        #もう一度graphへオブジェクトを渡して変更分の値は参照されないようにした。
        a = s[1]
        a -= 1
        graph2 = copy.deepcopy(graph)
        #print(graph2)
        #print(graph[a])
        for x in graph[a]:
            for xi in graph[x]:
                if xi != a:
                    graph2[a].append(xi)
        graph = graph2
    #print(graph)

#print(graph)

for i in range(n):
    ynlist = []
    for j in range(n):
        if j in graph[i]:
            ynlist.append("Y")
        else:
            ynlist.append("N")
    print(*ynlist, sep="")
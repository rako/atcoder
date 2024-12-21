"""
「選んだビルたちは等間隔に並んでいる」とは、「選んだビルの添字を i[1]<i[2]<...<i[k] としたとき、i[2]-i[1]=i[3]-i[2]=...=i[k]-i[k-1]を満たす」という意味です。
2つのビルは常に等間隔に並んでいるとみなします。
"""

n = int(input())
h = list(map(int,input().split()))
hindex = {}
for i,j in enumerate(h):
    if j not in hindex:
        hindex[j] = []
    hindex[j].append(i)
#print(hindex)
flag = 0
count = 0
for value in hindex.values(): #値のリストを取り出す
    if len(value) >= 3: #3つ以上のビルが等間隔に並んでいる場合
        for i in range(len(value)): #値のリストの中身を取り出す。i番目
            count = 0
            hop = 1
            tmp = 1
            while True:
                if i + hop >= len(value):
                    break
                diff = value[i+hop] - value[i]
                x = i + hop
                while True:
                    if x + hop >= len(value):
                        break
                    if value[x+hop] - value[x] == diff:
                        x += hop
                        tmp += 1
                    else:
                        break
                hop += 1
            count = max(count, tmp)
    else:
        flag += 1
        continue
if flag == len(hindex):
    print(1)
else:
    print(count + 2)
from collections import defaultdict,Counter

n = int(input())

ssl = [Counter(sorted(input())) for _ in range(n)]

if n != 1:
    ans = Counter()
    for i in range(n-1):
        for j in range(i+1,n):
            if i == 0 and j == 1:
                ans += (ssl[i] & ssl[j])
            else:
                ans &= (ssl[i] & ssl[j])
    result = ""
    for i in ans:
        result += i*ans[i]
    print("".join(sorted(result)))

else:
    ans = ssl[0]
    result = ""
    for i in ans:
        result += i*ans[i]
    print("".join(sorted(result)))

"""
s = []

for i in range(n):
    si = sorted(input())
    s.append(si)

ssl = []

#n個の文字列を辞書型にしてカウント
for i in s:
    ss = defaultdict(int)
    for j in i:
        ss[j] += 1
    ssl.append(ss)
"""

"""
ans = defaultdict(int)

#n個の辞書から一つずつ取り出して、全部の文字列に合ってその個数の中で最小値を格納
for i in range(n-1):
    for j in range(i+1,n): #全組み合わせn*(n-1)/2
        for k in ssl[i]:#sslのi番目のキーk番目
            print(i,j,k)
            if k in ssl[j]: #組み合わせ内で同じものがあれば
                if k in ans: #既に答えリストの中にあれば
                    ans[k] = min(ssl[i][k], ssl[j][k], ans[k])
                else:
                    ans[k] = min(ssl[i][k], ssl[j][k])
            else: #無くて、答えリストにあれば削除
                if k in ans:
                    del ans[k]

                    
result = ""
for i in ans:
    result += i*ans[i]

print("".join(sorted(result)))
"""
s = input()
from itertools import groupby
ans = 0
sg = groupby(s)
for key, group in sg:
    g = len(list(group))
    #print(key, g)
    if key == '0': #ナニコレ、なんか変な感じになってる。
        if g % 2 == 0:
            ans += g// 2
        else:
            ans += (g // 2 ) + 1
    else:
        ans += g
    #print(ans)
print(ans)
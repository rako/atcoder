import itertools
n,k = map(int, input().split())
s = input()
ans = 0
for key, value in itertools.groupby(s):
    #print(key, len(list(value)))
    if key == "O":
        ans += len(list(value)) // k
print(ans)
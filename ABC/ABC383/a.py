n = int(input())
time = 0
ans = 0
for i in range(n):
    t, v = map(int, input().split())
    ans1 = ans - (t- time)
    if ans1 > 0:
        ans = ans1
    else:
        ans = 0
    #print("ans",ans, "time", time)
    time = t
    ans += v
print(ans)
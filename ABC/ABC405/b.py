n,m = map(int, input().split())
a = list(map(int, input().split()))

def kansu():
    for number in range(1, m+1):
        if number not in a:
            return False
    return True

ans = 0
while (True):
    if kansu() == False:
        break
    a.pop(-1)
    ans += 1

print(ans)
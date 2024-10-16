from collections import defaultdict

n = int(input())

num = defaultdict(int)
for i in range(n):
    s = input()
    num[s] += 1

print(len(num))
import itertools

n = int(input())

a = list(map(int, input().split()))

listed = list(itertools.combinations_with_replacement(a ,2))

count = 0
for i in listed:
    if i[0] != i[1]:
        count += 1

print(count)
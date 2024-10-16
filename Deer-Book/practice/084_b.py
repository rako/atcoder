a, b = map(int, input().split())

s = input()

if all(map(str.isnumeric,s[:a])) and all(map(str.isnumeric,s[-b:])) and s[a] == "-":
    print("Yes")
else:
    print("No")
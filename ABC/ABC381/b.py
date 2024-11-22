import collections
s = input()

exist1 = 0
exist2 = 1
exist3 = 1
if len(s) % 2 == 0:
    exist1 = 1
for i in range(len(s)//2):
    if s[2* i] != s[2*i+1]:
        exist2 = 0
c = collections.Counter(s)
for value in c.values():
    if value != 2:
        exist3 = 0
print("Yes" if exist1 * exist2 * exist3 == 1 else "No")
#print(exist1, exist2, exist3)
import copy
a = list(input().split())
c = sorted(a)
for i in range(len(a) - 1):
  b = copy.deepcopy(a)
  b[i], b[i+1] = b[i+1], b[i]
  #print(b)
  if c == b:
    print("Yes")
    exit()
print("No")
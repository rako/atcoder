import itertools
n = int(input())
s = input()
sb = itertools.groupby(s)
groups = []
for key, group in sb:
  groups.append([key, len(list(group))])

if len(groups) == 1 or len(groups) == 2:
  print(0)
  exit()

mid = len(groups)//2
if groups[mid][0] == "0":
  mid += 1

#print(mid)
#print(groups)

#for key, length in groups:
  #print(key, length)

pointer = 0
pointerV = 0

k = mid
ans = 0

t2 = 0
while(True):
  k += 1
  if len(groups) <= k:
    break
  if groups[k][0] == "0":
    t2 += groups[k][1]
  else:
    if groups[k][1] <= t2:
      ans += t2
    else:
      if groups[k][1] >= pointerV:
        pointer = k
        pointerV = groups[k][1]
      break
  #print("k", k, "ans", ans)

k = mid
t1 = 0
while (True):
  k -= 1
  if k < 0:
    break
  if groups[k][0] == "0":
    t1 += groups[k][1]
  else:
    if groups[k][1] <= t1:
      ans += t1
    else:
      if groups[k][1] >= pointerV:
        pointer = k
        pointerV = groups[k][1]
      break
  #print("k", k, "ans", ans)

if pointer == 0 and pointerV == 0:
  print(ans)
  exit()

k = pointer
ans = 0
t2 = 0
while(True):
  k += 1
  if len(groups) <= k:
    break
  if groups[k][0] == "0":
    t2 += groups[k][1]
  else:
    if groups[k][1] <= t2:
      ans += t2

k = pointer
t1 = 0
while (True):
  k -= 1
  if k < 0:
    break
  if groups[k][0] == "0":
    t1 += groups[k][1]
  else:
    if groups[k][1] <= t1:
      ans += t1


print(ans)
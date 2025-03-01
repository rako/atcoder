n, q = map(int, input().split())
birddict = {i:i for i in range(n)}
nest = [[i] for i in range(n)]
ans = []
for i in range(q):
  op = input().split()
  if op[0] == "1":
    a, b = map(int, op[1:])
    a -= 1
    b -= 1
    location = birddict[a]
    #print("location", location, "a", a, "b", b)
    nest[location].remove(a)
    nest[b].append(a)
    birddict[a] = b
  elif op[0] == "2":
    a, b = map(int, op[1:])
    a -= 1
    b -= 1
    tmpa = nest[a]
    tmpb = nest[b]
    #print("tmpa", tmpa, "tmpb", tmpb)
    for i in tmpa:
      birddict[i] = b
    for i in tmpb:
      birddict[i] = a
    nest[a] = tmpb
    nest[b] = tmpa
  elif op[0] == "3":
    a = int(op[1])
    a -= 1
    ans.append(birddict[a]+1)
  #print("nest", nest)
for ans1 in ans:
  print(ans1)
#print(birddict)
#print(nest)
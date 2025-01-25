import itertools,copy

n = int(input())
a = list(map(int, input().split()))
nl = [i for i in range(n)]
tmp = [a]
donelist = []
anslist = []

while(len(tmp) > 0):
  tmp2 = copy.deepcopy(tmp)
  tmp3 = []
  for i in tmp:
    # XOR
    if i in donelist:
      continue
    donelist.append(i)
    xorans = 0
    for j in i:
      xorans = xorans ^ j
    if xorans not in anslist:
      anslist.append(xorans)
    else:
      tmp2.remove(i)


    # 新しい配列を作る
    tmp1 = []
    for k in list(itertools.combinations(nl, 2)):
      b = copy.deepcopy(i)
      b[k[1]] += b[k[0]]
      b[k[0]] = 0
      b.sort()
      if b not in donelist:
        tmp1.append(b)
    #print("tmp1", tmp1)
    tmp3 += tmp1

  tmp = []
  for j in tmp3:
    if j not in donelist and j not in tmp2:
      tmp.append(j)
  for l in tmp2:
    if l not in donelist:
      tmp.append(l)
  # XORあったら削除したものをtmpにしてもう一度やる
  #print("donelist", donelist)


print(len(anslist))
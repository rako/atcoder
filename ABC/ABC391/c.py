import collections
n,q = map(int,input().split())
"""
bl = {}
for k in range(1,n+1):
  bl[str(k)] = k
ans = []
for i in range(q):
  query = list(input().split())
  if query[0] == "1":
    p,h = int(query[1]), int(query[2])
    p = str(p)
    bl[p] = h
  elif query[0] == "2":
    value_counts = collections.Counter(bl.values())
    #print(value_counts)
    count = sum(1 for v in value_counts.values() if v >= 2)
    ans.append(count)
"""

bl = {}
for k in range(n):
  bl[str(k)] = k
bln = [1] * n
ans = []
total = 0
for i in range(q):
  query = list(input().split())
  if query[0] == "1":
    # 入力処理
    p,h = int(query[1]), int(query[2])
    p -= 1
    h -= 1

    # 元の巣の値を取得
    blpn = bl[str(p)]

    # 巣の数をチェック
    if bln[blpn] == 1:
      if bln[h] == 0:
        total += 0
      elif bln[h] == 1:
        total += 1
      elif bln[h] >= 2:
        total += 0
    elif bln[blpn] == 2:
      if bln[h] == 0:
        total -= 1
      elif bln[h] == 1:
        total += 0
      elif bln[h] >= 2:
        total -= 1
    elif bln[blpn] >= 3:
      if bln[h] == 0:
        total += 0
      elif bln[h] == 1:
        total += 1
      elif bln[h] >= 2:
        total += 0
    
    # 次の巣の数を増やす
    bln[h] += 1

    # 元の巣の数を減らす
    bln[blpn] -= 1
    
    # 巣を移動
    bl[str(p)] = h

  elif query[0] == "2":
    ans.append(total)
  #print(bl)
  #print(bln)


for q in ans:
  print(q)
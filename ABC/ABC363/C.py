N, K = map(int, input().split())

S = input()

from itertools import permutations 


st = set()
for it in permutations(S):
    st.add("".join(it))

#動的計画法？
for i in sorted(st):
    count = 0
    for j in list(i):
        if j == j-1:
            count += 1
        

"""
count = 0
start = 0
end = len(S) - 1
while start < end:
    if(S[start] == S[end]):
        start = start + 1
        end = end - 1
    else:
        break
if(start >= end):
    count += 1
else:
    pass
"""
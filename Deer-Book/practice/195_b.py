import math

a,b,w = map(int, input().split())

if math.floor(w//a) + 1 == math.ceil(w//b):
    pass

for i in range(w//a + 1):
    for j in range(w//b + 1):
        pass
k = int(input())

a, b = map(int, input().split())

exist = False
for i in range(a, b+1):
    if i % k == 0:
        exist = True
    
if exist == True:
    print("OK")
else:
    print("NG")
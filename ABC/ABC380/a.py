n = list(input())
count1 = 0
count2 = 0
count3 = 0
for i in n:
    if i == '1':
        count1 += 1
    elif i == '2':
        count2 += 1
    elif i == '3':
        count3 += 1
if count1 == 1 and count2 == 2 and count3 == 3:
    print("Yes")
else:
    print("No")
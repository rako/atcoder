A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

flag = 0
if (B[0] - A[0] == 0) and ((C[1] - B[1] == 0) or (A[1] - C[1] == 0)):
    flag = 1
elif (C[0] - B[0] == 0) and ((A[1] - C[1] == 0) or (B[1] - A[1] == 0)):
    flag = 1
elif (A[0] - C[0] == 0) and ((B[1] - A[1] == 0) or (C[1] - B[1] == 0)):
    flag = 1
else:
    flag = 0
    AB = (B[1] - A[1])/(B[0] - A[0])
    BC = (C[1] - B[1])/(C[0] - B[0])
    CA = (A[1] - C[1])/(A[0] - C[0])

if (flag == 1):
    print("Yes")
elif (flag == 0):
    if ((AB * BC == -1) or (BC * CA == -1) or (CA * AB == -1)):
        print("Yes")
    else:
        print("No")
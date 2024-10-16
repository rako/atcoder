h, w = map(int, input().split())

imglist = [list(input()) for _ in range(h)]

for i in range(h * 2):
    imglist2 = []
    for k in range(w):
        imglist2.append(imglist[i//2][k])
    print("".join(imglist2))

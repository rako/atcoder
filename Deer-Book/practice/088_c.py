c = []
for _ in range(3):
    c.append(list(map(int, input().split())))

while(True):
    for i in range(3):
        minnumrow = 100
        for j in range(3):
            minnumrow = min(minnumrow, c[j][i])
        for k in range(3):
            c[k][i] -= minnumrow
    for i in range(3):
        minnumcol = 100
        for j in range(3):
            minnumcol = min(minnumcol, c[i][j])
        for k in range(3):
            c[i][k] -= minnumcol
    #行列の全ての列行で全部0か、要素が全部0か判定
    mcol = 0
    mrow = 0
    notzeroexist = False
    for i in range(3):
        minnumcol = 100
        minnumrow = 100
        for j in range(3):
            minnumcol = min(minnumcol, c[i][j])
            minnumrow = min(minnumrow, c[j][i])
            if c[i][j] != 0:
                notzeroexist = True
        if minnumcol != 0:
            mcol = 1
        if minnumrow != 0:
            mrow = 1
    if mcol == mrow == 0:
        if notzeroexist:
            print("No")
            break
        else:
            print("Yes")
            break
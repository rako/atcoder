sx, sy = map(int, input().split())
tx, ty = map(int, input().split())

fee = 0

if abs(tx - sx) <= abs(ty - sy):
    fee = abs(ty - sy)
else:
    if abs(tx - sx)%2 == 1:
        fee = abs(ty - sy) + abs(tx - sx) + 1
    else:
        fee = abs(ty - sy) + abs(tx - sx)
    

print(fee)

"""
if (sx + sy)//2 == 0: #偶数の場合
    if (tx - sx)//2 == 0:
        if (ty - sy)//2 == 0: #xy共に偶数
            
        else: #x偶数, y奇数

    else: #x奇数
        if (ty - sy)//2 == 0:

        else:
            
"""
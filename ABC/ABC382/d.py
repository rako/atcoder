import copy

n,m = map(int, input().split())

ans = []

base = 1
while(True):
    base_list = []
    for i in range(n):
        base_list.append(base + 10*(i))
    if base_list[-1] > m:
        break
    #ここでbaseが変わらない時に無限ループで作り出す
    base_plus_list = copy.deepcopy(base_list)
    change_list(base_plus_list, k)
    
def change_list(changed_list, k):
    changed_list[-k] += changed_list[-k] + 1
    for i in range(n-m, n-1):
        changed_list[i+1] = changed_list[i] + 10
    return change_list
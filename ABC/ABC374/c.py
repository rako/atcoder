n = int(input())
k = list(map(int, input().split()))

# 部署の人数の合計
total_sum = sum(k)

# dp配列を初期化
dp = [False] * (total_sum + 1)
dp[0] = True

# 各部署の人数をグループAに割り当てるかグループBに割り当てるかを決定
for num in k:
    for j in range(total_sum, num - 1, -1):
        dp[j] = dp[j] or dp[j - num]

# 最小の最大グループの人数を求める
min_max_group_sum = total_sum
for i in range(total_sum // 2 + 1):
    if dp[i]:
        min_max_group_sum = min(min_max_group_sum, max(i, total_sum - i))

print(min_max_group_sum)
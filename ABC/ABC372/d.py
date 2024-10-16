import itertools
n = input()
h = list(map(int, input().split()))

def rank_elements(original_list):
    # 元のリストを（値、インデックス）の形でソート
    sorted_list = sorted(enumerate(original_list), key=lambda x: -x[1])
    
    # 新しいリストを作成して順位を割り当てる
    rank_list = [0] * len(original_list)
    current_rank = 1
    for i, (index, value) in enumerate(sorted_list):
        # 同じ値であれば同じ順位にする
        if i > 0 and value == sorted_list[i - 1][1]:
            rank_list[index] = current_rank - 1
        else:
            rank_list[index] = current_rank
        current_rank += 1

    return rank_list

result = rank_elements(h)

for i in range(n):
    print(n-i, sep="")
#print(f"元のリスト: {example_list}")
#print(f"順位リスト: {result}")

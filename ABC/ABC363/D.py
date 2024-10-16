n = int(input())

def is_palindrome(n):
    # 数字を文字列に変換し、それが回文かどうかをチェック
    return str(n) == str(n)[::-1]

def generate_palindromes(start, end):
    palindromes = []
    for i in range(start, end + 1):
        if is_palindrome(i):
            palindromes.append(i)
    return palindromes

def nth_palindrome(n, start=1, end=100000):
    palindromes = generate_palindromes(start, end)
    if n <= len(palindromes):
        return palindromes[n-2]
    else:
        return None  # 指定された範囲内にN番目の回文数が存在しない場合


nth_pal = nth_palindrome(n)
if nth_pal is not None:
    if n == 1:
        print(str(0))
    else:
        print(int(nth_pal))
else:
    pass

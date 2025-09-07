N = int(input())
S = input()

def f(s, x):
    c = 0
    l = list(s)
    t = [x, 'B' if x == 'A' else 'A'] * N
    
    for i in range(2 * N):
        if l[i] != t[i]:
            j = i + 1
            while j < 2 * N and l[j] != t[i]:
                j += 1
            while j > i:
                l[j], l[j-1] = l[j-1], l[j]
                j -= 1
                c += 1
    return c

a = f(S, 'A')
b = f(S, 'B')
print(min(a, b))

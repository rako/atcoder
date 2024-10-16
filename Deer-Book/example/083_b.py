n, a, b = map(int, input().split())

total2 = 0

for i in range(1, n+1):
    n1_a, n1_b = i // 10000, i % 10000
    n2_a, n2_b = n1_b // 1000, n1_b % 1000
    n3_a, n3_b = n2_b // 100, n2_b % 100
    n4_a, n4_b = n3_b // 10, n3_b % 10
    total = n1_a + n2_a + n3_a + n4_a + n4_b
    if a <= total and total <= b:
        total2 += i

print(total2)
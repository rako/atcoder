n,d = map(int, input().split())
snake = []
for i in range(n):
    t,l = map(int, input().split())
    snake.append([t,l])
ans = []
for k in range(1,d+1):
    snake2 = []
    for i in range(n):
        total = (snake[i][1] + k) * snake[i][0]
        snake2.append(total)
    ans.append(max(snake2))
for a in ans:
    print(a)
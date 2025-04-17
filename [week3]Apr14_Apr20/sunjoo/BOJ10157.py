C, R = map(int, input().split())
K = int(input())

adj = [[] for _ in range(C+1)]
delta = [(0, 1), (1, 0), (0, -1), (-1, 0)]
direction = 0
x = y = 1
cnt = 1

if K > C*R:
    print(0)
else:
    while cnt < K:
        adj[x].append(y)
        dx, dy = delta[direction]
        nx, ny = x + dx, y + dy
        if nx < 1 or nx > C or ny < 1 or ny > R or ny in adj[nx]:
            direction = (direction + 1) % 4
            continue
        x, y = nx, ny
        cnt += 1

    print(x, y)
from collections import deque

def bfs():
    q.append((1, 1))

    while q:
        y, x = q.pop()
        visited[y][x] = 1
        for dy, dx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ny, nx = y + dy, x + dx
            if arr[ny][nx] == 3:
                return 1
            if ny < 1 or ny >= 14 or nx < 1 or nx >= 14:
                continue
            if arr[ny][nx] == 1:
                continue
            if visited[ny][nx] == 1:
                continue
            q.append((ny, nx))

    return 0


T = 10
for _ in range(T):
    tc = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    q = deque()
    visited = [[0] * 16 for _ in range(16)]
    result = bfs()

    print(f'#{tc} {result}')
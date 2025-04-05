from collections import deque

T = int(input())

def bfs(a, b):
    q = deque()
    q.append((a, b))
    arr[a][b] = 0

    while q:
        r, c = q.popleft()
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r+dr, c+dc
            if nr < 0 or nr >= N or nc < 0 or nc >= M or arr[nr][nc] ==0: 
                continue
            q.append((nr, nc))
            arr[nr][nc] = 0

for tc in range(1, T+1):
    M, N, K = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    lst = []
    for _ in range(K):
        X, Y = map(int, input().split())
        arr[Y][X] = 1
        lst.append((Y, X))

    cnt = 0
    for y, x in lst:
        if arr[y][x] == 1:
            bfs(y, x)
            cnt += 1

    print(cnt)
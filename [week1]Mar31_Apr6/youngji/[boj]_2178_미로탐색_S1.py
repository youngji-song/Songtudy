# 2178번 미로 탐색 Silver I
# 22:55 ~ 23:08

from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(n)]

# (0,0)에서 시작
r, c = 0, 0

# deque
q = deque()
q.append([r,c])

visited = [[0 for _ in range(m)] for _ in range(n)]
visited[r][c] = 1

while q:
    r, c = q.popleft()
    for dr, dc in [[0,1],[1,0],[0,-1],[-1,0]]:
        nr, nc = r + dr, c + dc
        
        if 0>nr or nr>=n or 0>nc or nc>=m:
            continue
        if maze[nr][nc] == 0:
            continue
        if visited[nr][nc]:
            continue
        visited[nr][nc] = visited[r][c]+1
        q.append([nr,nc])

print(visited[n-1][m-1])
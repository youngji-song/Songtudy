# 7569 토마토 Gold V

'''
인접한 토마토 = 위, 아래, 왼쪽, 오른쪽, 앞, 뒤 (6방향)
보관된 토마토들이 며칠이 지나야 다 익는지 "최소 일수"

상자의 일부 칸에는 토마토가 없을 수도 있음

m: 가로, n: 세로, h: 높이
1: 익은 토마토, 0: 익지 않은 토마토, -1: 토마토 없음

원래 위치 = r, c
위: r-n, c
아래: r+n, c
왼쪽: r, c-1
오른쪽: r, c+1
앞: r-1, c
뒤: r+1, c
'''

from collections import deque

m, n, h = map(int, input().split())
tomatoes = [list(map(int, input().split())) for _ in range(n*h)]

q = deque()
visited = [[-1 for _ in range(m)] for _ in range(n*h)]

# 모든 익은 토마토에서 bfs
for i in range(n*h):
    for j in range(m):
        if tomatoes[i][j] == 1:
            q.append((i,j))
            visited[i][j] = 0

while q:
    r, c = q.popleft()
    
    # 위, 아래/ 왼쪽, 오른쪽, 상, 하
    for dr, dc in [[-n,0],[n,0],[0,-1],[0,1],[-1,0],[1,0]]:
        nr, nc = r + dr, c + dc
        # 각 층의 테두리에서 상,하로 움직일 때 -> 사실 불가능
        if (r+1)%n == 0 and dr == 1:
            continue
        elif r%n == 0 and dr == -1:
            continue

        # out of index
        if nr<0 or nr>=n*h or nc<0 or nc>=m:
            continue

        # 토마토가 없는 곳
        if tomatoes[nr][nc] == -1:
            continue
        
        # 이미 방문 한 곳
        if visited[nr][nc] != -1:
            continue

        if tomatoes[nr][nc] == 0:
            tomatoes[nr][nc] = 1
            q.append((nr,nc))
            visited[nr][nc] = visited[r][c] + 1

ans = 0
# 남은 익지 않은 토마토가 있는지?
for i in range(n*h):
    for j in range(m):
        if tomatoes[i][j] == 0:
            ans = -1
            break
        
if ans!= -1:
    for i in range(n*h):
        for j in range(m):
            ans = max(ans,visited[i][j])

print(ans)
# print(visited)
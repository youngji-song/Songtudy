# 0=길, 1=벽, 2=출발점, 3=도착점
# visited 만들어서 방문체크 / bfs
# 상하좌우에 벽이 아니고 visited안갔으면 가고 1체크

from collections import deque

def bfs(x,y):
    q = deque()
    visited = [[0]*16 for _ in range(16)]

    q.append((x,y))
    visited[x][y] = 1

    while q:
        r, c = q.popleft()

        if arr[r][c] == 3:
            return 1

        for r_dir, c_dir in ((-1,0), (0,1), (1,0), (0,-1)):
            nr = r + r_dir
            nc = c + c_dir
            if 0 <= nr < 16 and 0 <= nc < 16 and visited[nr][nc] == 0 and arr[nr][nc] != 1:
                q.append((nr,nc))
                visited[nr][nc] = 1
    return 0

t = 10

for tc in range(1,t+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    answer = 0

    for i in range(16):
        for j in range(16):
            if arr[i][j] == 2:
                start_x = i
                start_y = j
    
    answer = bfs(start_x, start_y)

    print(f'#{tc} {answer}')
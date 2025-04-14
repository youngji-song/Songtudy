# 1726 로봇 G3

'''
명령1: Go k: 현재 향하고 있는 방향을 k칸 움직임 (k = {1, 2, 3})
명령2: Turn dir: 왼쪽/오른쪽으로 90도 회전 (dir = left or right)

궤도
- 0: 로봇이 갈 수 있는 곳
- 1: 로봇이 갈 수 없는 곳
'''

from collections import deque

m, n = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(m)]
sr, sc, sd = map(int, input().split())
sr, sc, sd = sr-1, sc-1, sd-1
er, es, ed = map(int, input().split())
er, es, ed = er-1, es-1, ed-1

q = deque()
q.append((sr, sc, sd, 0))
visited = [[0 for _ in range(n)] for _ in range(m)]
visited[sr][sc] = 0

# 동(0), 서(1), 남(2), 북(3)
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

while q:
    r, c, d, k = q.popleft()
    # 현위치_row, 현위치_col, 현재방향, 같은 방향으로 움직인 횟수

    # 목적지에 도착
    if (r, c) == (er, es):
        # 방향도 일치
        if d == ed:
            break
        # 방향이 다름
        elif d != ed:
            # 두 번 회전해야하는 경우
            if (d,ed) in [(0,1),(1,0),(2,3),(3,2)]:
                visited[er][es] += 2
            # 한 번만 회전하면 되는 경우
            else:
                visited[er][es] += 1
            break

    # 탐색
    for p in range(4):
        nr, nc = r + dr[p], c + dc[p]

        # out of index
        if 0>nr or nr>=m or 0>nc or nc>=n:
            continue

        # already visited
        if visited[nr][nc]:
            continue

        if board[nr][nc] == 1:
            continue

        # 이전과 같은 방향
        if d == p:
            if k < 3:
                q.append((nr, nc, p, k+1))
                visited[nr][nc] = visited[r][c]
            else:
                q.append((nr, nc, p, 0))

        elif (d,p) in [(0,1),(1,0),(2,3),(3,2)]:# 마주보는 방향 -> 2회 회전:
            q.append((nr, nc, p, 0))
            visited[nr][nc] = visited[r][c] + 3
        else:   # 1회 회전
            q.append((nr, nc, p, 0))
            visited[nr][nc] = visited[r][c]+2

        for row in visited:
            print(row)
        print()

print(visited[er][es])
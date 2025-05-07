from collections import deque

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs(sy, sx):
    visited = [[False] * N for _ in range(N)]
    q = deque()
    q.append((sy, sx, 0))  # y, x, 거리
    visited[sy][sx] = True
    fishes = []
    min_dist = float('inf')

    while q:
        y, x, dist = q.popleft()

        # 더 먼 거리면 의미 없음
        if dist > min_dist:
            break

        for dir in range(4):
            ny = y + dy[dir]
            nx = x + dx[dir]

            if not (0 <= ny < N and 0 <= nx < N):
                continue
            if visited[ny][nx]:
                continue
            if graph[ny][nx] > srk:
                continue

            visited[ny][nx] = True

            if 0 < graph[ny][nx] < srk:
                fishes.append((dist + 1, ny, nx))
                min_dist = dist + 1
            else:
                q.append((ny, nx, dist + 1))

    fishes.sort()
    if fishes:
        dist, fy, fx = fishes[0]
        return (fy, fx, dist)
    else:
        return None

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

srk = 2  # 아기상어 초기 크기
cnt = 0  # 먹은 물고기 수
distance = 0  # 총 이동 거리

# 아기상어 시작 위치
for y in range(N):
    for x in range(N):
        if graph[y][x] == 9:
            sy, sx = y, x
            graph[y][x] = 0

while True:
    result = bfs(sy, sx)
    if not result:
        break

    sy, sx, dist = result
    graph[sy][sx] = 0
    distance += dist
    cnt += 1

    # 아기상어 크기 키우기
    if cnt == srk:
        srk += 1
        cnt = 0

print(distance)

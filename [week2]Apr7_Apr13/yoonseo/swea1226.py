from collections import deque


def bfs():
    q = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q.append([1,1])

    while q:
        now_x, now_y = q.popleft()
        graph[now_x][now_y] = 1

        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if 0 <= nx < 16 and 0 <= ny < 16 and graph[nx][ny] == 0:
                q.append([nx, ny])
                graph[nx][ny] = 1
            elif graph[nx][ny]==3:
                return 1


for tc in range(1, 11):
    n = input()
    graph = [list(map(int, input().strip())) for _ in range(16)]

    print(f'#{tc} {1 if bfs() else 0}')
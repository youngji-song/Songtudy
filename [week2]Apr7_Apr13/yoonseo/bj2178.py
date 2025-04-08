from collections import deque

def bfs(x,y):
    q = deque()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    q.append((x,y))

    while q:
        now_x, now_y = q.popleft()
        for i in range(4):
            next_x = now_x + dx[i]
            next_y = now_y + dy[i]
            if 0 <= next_x < N and 0 <= next_y < M and graph[next_x][next_y] == 1:
                graph[next_x][next_y] = graph[now_x][now_y] + 1
                q.append((next_x, next_y))
    return graph[N-1][M-1]



N, M = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]
print(bfs(0,0))
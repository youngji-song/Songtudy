from collections import deque

# ---------------- BFS로 섬 번호 매기기 ----------------
def bfs(sr, sc, cnt):
    q = deque()
    q.append((sr, sc))
    visited[sr][sc] = cnt

    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 1 and visited[nr][nc] == 0:
                visited[nr][nc] = cnt
                q.append((nr, nc))

# ---------------- 유니온 파인드 ----------------
def find_set(x):
    if x == parents[x]:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]

def union(x, y):
    rx = find_set(x)
    ry = find_set(y)
    if rx != ry:
        if rx < ry:
            parents[ry] = rx
        else:
            parents[rx] = ry

# ---------------- 입력 및 섬 분리 ----------------
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

cnt = 1
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and visited[i][j] == 0:
            bfs(i, j, cnt)
            cnt += 1

V = cnt - 1  # 섬의 개수

# ---------------- 다리 후보 추출 ----------------
graph = []

for i in range(N):
    for j in range(M):
        if visited[i][j] > 0:
            s = visited[i][j]

            # 오른쪽
            length = 0
            for nj in range(j + 1, M):
                if visited[i][nj] == 0:
                    length += 1
                elif visited[i][nj] != s:
                    if length >= 2:
                        e = visited[i][nj]
                        graph.append((s, e, length))
                    break
                else:
                    break

            # 왼쪽
            length = 0
            for nj in range(j - 1, -1, -1):
                if visited[i][nj] == 0:
                    length += 1
                elif visited[i][nj] != s:
                    if length >= 2:
                        e = visited[i][nj]
                        graph.append((s, e, length))
                    break
                else:
                    break

            # 아래쪽
            length = 0
            for ni in range(i + 1, N):
                if visited[ni][j] == 0:
                    length += 1
                elif visited[ni][j] != s:
                    if length >= 2:
                        e = visited[ni][j]
                        graph.append((s, e, length))
                    break
                else:
                    break

            # 위쪽
            length = 0
            for ni in range(i - 1, -1, -1):
                if visited[ni][j] == 0:
                    length += 1
                elif visited[ni][j] != s:
                    if length >= 2:
                        e = visited[ni][j]
                        graph.append((s, e, length))
                    break
                else:
                    break

# ---------------- 크루스칼 알고리즘 ----------------
edges = sorted(graph, key=lambda x: x[2])
parents = [i for i in range(V + 1)]

result = 0
cnt_edge = 0

for start, end, weight in edges:
    if find_set(start) != find_set(end):
        union(start, end)
        result += weight
        cnt_edge += 1
        if cnt_edge == V - 1:
            break

# 연결 안 된 섬이 있는지 체크
root = find_set(1)
for i in range(2, V + 1):
    if find_set(i) != root:
        print(-1)
        break
else:
    print(result)

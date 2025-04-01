from collections import deque

N, M, R = map(int, input().split())
arr = [[] for _ in range(N+1)]          # 2차원 배열 메모리 초과 >>> arr list 로 변경
for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)
visited = [0] * (N+1)
q = deque()


def bfs(r):
    visited[r] = 1
    q.append(r)
    cnt = 2
    while q:
        k = q.popleft()
        arr[k].sort()
        for i in arr[k]:
            if visited[i] > 0:
                continue
            visited[i] = cnt
            cnt += 1
            q.append(i)


bfs(R)
for i in range(1, N+1):
    print(visited[i])
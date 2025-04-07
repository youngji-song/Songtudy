from collections import deque

def bfs(N):
    q = deque()
    q.append(N)
    while q:
        now = q.popleft()
        if now == K:
            return visited[K]
        for next in (now-1, now+1, now*2):
            if 0 <= next <= limit and not visited[next]:
                visited[next] = visited[now]+1
                q.append(next)

limit = 10**5
N, K = map(int, input().split())
visited = [0]*(limit+1)
print(bfs(N))
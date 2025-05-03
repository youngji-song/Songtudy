import heapq

N, M = map(int, input().split())

indegree = [0] * (N+1)
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)
    indegree[B] += 1

pq = []
result = []

for i in range(1, N+1):
    if indegree[i] == 0:
        heapq.heappush(pq, i)

while pq:
    now = heapq.heappop(pq)
    result.append(now)
    for nxt in graph[now]:
        indegree[nxt] -= 1
        if indegree[nxt] == 0:
            heapq.heappush(pq, nxt)

print(*result)
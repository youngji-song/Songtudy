import heapq, sys

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
INF = int(21e8)

graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for b, c in graph[now]:
            min_dist = dist + c
            if min_dist < distance[b]:
                distance[b] = min_dist
                heapq.heappush(q, (min_dist, b))

dijkstra(K)

for i in range(1, V+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])
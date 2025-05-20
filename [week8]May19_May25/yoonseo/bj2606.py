N = int(input())
v = int(input())
graph = [[] for _ in range(N+1)]
visited = [False]*(N+1)

for i in range(v):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def dfs(s):
    visited[s]=1
    for ns in graph[s]:
        if not visited[ns]:
            dfs(ns)

dfs(1)
print(sum(visited)-1)
# 10451 순열 사이클 실버 3
# 12:30 ~ 13:15

t = int(input())
for tc in range(t):
    n = int(input())
    graph = list(map(int, input().split()))
    graph.insert(0,0)
    visited = [0 for _ in range(n+1)]


    for i in range(1,n+1):
        if visited[i]:
            continue
        if i == graph[i]:
            visited[i] = i
        else:
            parent = i
            while True:
                if visited[graph[i]] == parent:
                    break
                visited[graph[i]] = parent
                i = graph[i]

    print(len(set(visited))-1)
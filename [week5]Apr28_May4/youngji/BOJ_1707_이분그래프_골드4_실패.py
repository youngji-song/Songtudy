# 1707 이분_그래프 골드4
# 23:00 ~

from collections import defaultdict, deque

k = int(input())
for tc in range(k):
    node, edge = map(int, input().split())
    graph = defaultdict(list)

    for i in range(edge):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [-1 for _ in range(node+1)]
    visited[1] = 0

    # q = deque()
    # q.append(1)
    q2 = set()
    q2.add(1)

    result = 'YES'
    for i in range(1,node+1):
        for end in graph[i]:
            if end in q2:
                continue
            if visited[end] == visited[i]:
                result = 'NO'
                break
            visited[end] = 1 - visited[i]
            q2.add(end)

    print(result)

'''    while q:
        start = q.popleft()
        for end in graph[start]:
            if visited[end] == visited[start]:
                result = 'NO'
                break
            visited[end] = 1- visited[start]
            if end not in q2:
                q.append(end)
                q2.add(end)
    # print(visited)
    if len(q2) != node:
        result = 'NO'
    print(result)'''
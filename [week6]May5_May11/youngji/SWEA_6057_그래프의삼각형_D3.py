from collections import defaultdict

t = int(input())
for tc in range(1,t+1):
    n, m = map(int, input().split())
    graph = defaultdict(set)

    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].add(y)
        graph[y].add(x)

    triangles = set()
    for value1 in graph:
        for value2 in graph[value1]:
            for value3 in graph[value2]:
                if value3 == value1:
                    continue
                if value1 in graph[value3]:
                    triangle = [value1, value2, value3]

                    triangles.add(tuple(sorted(triangle)))

    print(f'#{tc}', len(triangles))
N = int(input())
graph = [[] for _ in range(N+1)]
time = [0] * (N+1)
for idx in range(N):
    building = list(map(int, input().split()))
    for i, b in enumerate(building):
        if b == -1:
            break
        if i == 0:
            time[idx+1] = b
            continue
        graph[idx+1].append(b)

for d in range(1, N+1):
    if graph[d]:
        for before in graph[d]:
            time[d] += time[before]

time.pop(0)

for t in time:
    print(t)
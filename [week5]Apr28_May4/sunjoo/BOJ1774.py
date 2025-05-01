from math import sqrt

def find(x):
    if x == parents[x]:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    ref_x = find(x)
    ref_y = find(y)

    if ref_x == ref_y:
        return False

    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y
    return True

N, M = map(int, input().split())

position = [(0, 0)]
for _ in range(N):
    X, Y = map(int, input().split())
    position.append((X, Y))

parents = [i for i in range(N+1)]
edges = []
cnt = 0
length = 0
init = 0

for _ in range(M):
    a, b = map(int, input().split())
    if union(a, b):
        init += 1

for i in range(1, N):
    for j in range(i+1, N+1):
        edges.append((i, j, sqrt(((position[i][0] - position[j][0]) ** 2) + (position[i][1] - position[j][1]) ** 2)))

edges.sort(key=lambda x: x[2])

for x, y, d in edges:
    if find(x) == find(y):
        continue
    union(x, y)
    cnt += 1
    length += d

    if cnt == N - init - 1:
        break

answer = round(length, 2)
print("%.2f" %answer)
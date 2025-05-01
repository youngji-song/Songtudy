from math import sqrt

def find_set(x):
    if x == parents[x]:
        return x
    parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    ref_x = find_set(x)
    ref_y = find_set(y)

    if ref_x == ref_y:
        return

    if ref_x < ref_y:
        parents[ref_y] = ref_x
    else:
        parents[ref_x] = ref_y


n = int(input())

stars = [list(map(float, input().split())) for _ in range(n)]
edges = []

for i in range(n):
    for j in range(i+1, n):

        edges.append((i, j, sqrt((stars[i][0] - stars[j][0])**2 + (stars[i][1] - stars[j][1])**2)))

edges.sort(key=lambda x: x[2])
parents = [i for i in range(n+1)]
cost = 0
cnt = 0

for x, y, c in edges:
    if find_set(x) == find_set(y):
        continue
    union(x, y)
    cnt += 1
    cost += c

    if cnt == n-1:
        break

print(cost)
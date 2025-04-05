import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v):
    global cnt
    # print(f"진입 dfs(v={v}), cnt={cnt}")

    visited[v] = cnt
    cnt += 1
    for n in arr[v]:
        # print(f"현재 {v}, 방문중 이웃 {n}, {visited[n]}")
        if visited[n] > 0:
            continue
        dfs(n)
    # print(f"나간다 dfs(v={v}, cnt={cnt}")
    return

N, M, R = map(int, input().split())
arr = [[] for _ in range(N+1)]        
visited = [0] * (N + 1)
for _ in range(M):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

for a in arr:
    a.sort()

cnt = 1
dfs(R)

for i in range(1, N+1):
    print(visited[i])
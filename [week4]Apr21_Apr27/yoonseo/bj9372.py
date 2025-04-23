import sys
input = sys.stdin.readline

def dfs(v):
    visited[v] = 1
    cnt = 0
    for i in airplane[v]:
        if not visited[i]:
            cnt += 1 + dfs(i)
    return cnt

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    airplane = [[] for _ in range(N+1)]
    visited = [0]*(N+1)

    for _ in range(M):
        a, b = map(int, input().split())
        airplane[a].append(b)
        airplane[b].append(a)
    
    print(dfs(1))
    
    

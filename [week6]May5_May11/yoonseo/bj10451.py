def dfs(s):
    visited[s]=1
    next = num[s]
    if not visited[next]:
        dfs(next)

T = int(input())
for tc in range(T):
    N = int(input())
    num = [0]+list(map(int, input().split()))
    visited = [0]*(N+1)
    visited[0] = 1
    cnt = 0

    for i in range(1, N+1):
        if not visited[i]:
            dfs(i)
            cnt+=1

    print(cnt)
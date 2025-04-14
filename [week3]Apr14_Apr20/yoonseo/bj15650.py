def dfs(start):
    if len(ans)==M:
        print(' '.join(map(str, ans)))
        return
    for i in range(start, N+1):
        if i not in ans:
            ans.append(i)
            dfs(i+1)
            ans.pop()

N, M = map(int, input().split())
ans = []
dfs(1)
def bfs(si,sj,N):
    global ans
    q = []
    q.append((si,sj))
    while q:
        r,c = q.pop(0)
        if abs(r-rock_x) + abs(c-rock_y) <= 1000:
            ans = 'happy'
            return
        for i in range(N):
            if visited[i] == 0:
                cu_x, cu_y = cu[i]
                if abs(r - cu_x) + abs(c-cu_y) > 1000:
                    continue
                visited[i] = 1
                q.append((cu_x,cu_y))


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    home_x, home_y = map(int,input().split())
    cu = [list(map(int,input().split())) for _ in range(N)]
    rock_x, rock_y = map(int,input().split())
    visited = [0]*(N+1)
    ans = 'sad'
    bfs(home_x,home_y,N)
    print(ans)
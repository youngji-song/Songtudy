# 석유 시추
# 21:25 ~

land = [[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]

# define dfs
def dfs(r, c, visited):
    global n, m, cnt  # cnt: 석유 몇 칸 있는가!

    # 4방 탐색
    for dr, dc in [[0,1],[1,0],[0,-1],[-1,0]]:
        nr, nc = r + dr, c + dc

        # out of index
        if nr<0 or nr>=n or nc<0 or nc>=m:
            continue
        # 석유가 아님
        if land[nr][nc] == 0:
            continue
        # 이미 방문
        if visited[nr][nc]:
            continue

        # 방문처리 후 (석유 +=1), dfs 돌기
        visited[nr][nc] = True
        cnt += 1
        dfs(nr, nc, visited)

def solution(land):
    n = len(land)   # row
    m = len(land[0])    # col

    max_cnt = 0     # 출력할 값
    # 각 col에 대해서 dfs 수행
    for j in range(m):
        visited = [[False for _ in range(m)] for _ in range(n)]
        cnt = 0
        # 각 row에 대해서 석유가 있고 이전에 방문한 적 없는 곳
        for i in range(n):
            if land[i][j] == 1 and not visited[i][j]:
                visited[i][j] = True
                cnt += 1
                dfs(i,j,visited)

        # 최댓값 갱신
        max_cnt = max(cnt, max_cnt)

    return max_cnt
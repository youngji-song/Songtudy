# bfs문제임
# 최단거리만 찾는게 아니라 횟수를 찾아야 함 
# -> 그러면 마지막 위치까지 +1한 값을 찾으면 됨
# -> 틀림 -1 하면 될듯

from collections import deque

n,m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]

def bfs(r,c):
    dr = [-1,0,1,0]
    dc = [0,1,0,-1]
    q = deque()
    q.append((r,c))
    
    while q:
        x, y = q.popleft()
        for i in range(4):
            nr, nc = x + dr[i], y + dc[i]
            
            if 0 <= nr < n and 0<= nc < m:
                if arr[nr][nc] == 1:
                    arr[nr][nc] = arr[x][y] + 1
                    q.append((nr, nc))
     
    return arr[n-1][m-1]

answer = bfs(0,0)

print(answer)
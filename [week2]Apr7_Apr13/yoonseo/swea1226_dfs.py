def dfs(x,y):
    global result
    dx, dy = [-1, 1, 0, 0],[0, 0, -1, 1]
 
    for i in dx:
        for j in dy:
            nx = x + i
            ny = y + j
            if maze[nx][ny] == 3:
                result = 1
                return
            if 0<= nx <16 and 0<= ny <16 and maze[nx][ny] == 0:
                maze[nx][ny] = 1
                dfs(nx,ny)
 
for _ in range(10):
    tc = input()
    maze = [list(map(int, input())) for _ in range(16)]
    result = 0
    dfs(1,1)
    print(f'#{tc} {result}')
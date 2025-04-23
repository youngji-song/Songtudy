def check(x,y):
    global N
    direction = [0]*4
    for d in range(4):
        length = 0
        for k in range(1,N):
            nx = x + dr[d]*k
            ny = y + dc[d]*k
            if 0<=nx<N and 0<=ny<N:
                length += 1
                if arr[nx][ny]:
                    length = 0
                    break
        direction[d] = length
    return direction
 
def connect(x,y,d):
    global N
    for k in range(1,N):
        nx = x + dr[d] * k
        ny = y + dc[d] * k
        if 0 <= nx < N and 0<= ny < N:
            arr[nx][ny] ^= 1
 
def recur(cur,min_sum,result_cnt):
    global result
    if result_cnt > result[0]:
        result[0] = result_cnt
        result[1] = min_sum
    elif result_cnt == result[0]:
        if result[1] > min_sum:
            result[1] = min_sum
    if cur == cnt:
        return
    x,y = core[cur][0], core[cur][1]
    direction = check(x,y)
    # print(direction)
    for d in range(4):
        if direction[d] == 0:
            continue
        connect(x,y,d)
        recur(cur+1,min_sum+direction[d],result_cnt+1)
        connect(x,y,d)
    recur(cur+1,min_sum,result_cnt)
 
 
 
 
 
 
T = int(input())
for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    core = []
    cnt = 0
    for i in range(1,N-1):
        for j in range(1,N-1):
            if arr[i][j] == 1:
                core.append((i,j))
                cnt += 1
    result = [0,0]
    recur(0,0,0)
    print(f'#{tc} {result[1]}')
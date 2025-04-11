def move(cur_com):
    global direction, cr, cc

    if cur_com == "A":
        dr, dc = delta[direction]
        nr, nc = cr + dr, cc + dc

        if nr < 0 or nr >= N or nc < 0 or nc >= N or field[nr][nc] == "T":
            return
        else:
            cr, cc = nr, nc

    elif cur_com == "L":
        direction = (direction - 1) % 4
    elif cur_com == "R":
        direction = (direction + 1) % 4


T = int(input())
for tc in range(1, T+1):
    N = int(input())        # 필드의 크기
    field = [list(input()) for _ in range(N)]
    Q = int(input())        # 조종 횟수
    command = [list(input().split()) for _ in range(Q)]

    delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]
    xr = xc = -1
    yr = yc = -1
    result = []


    for r in range(N):      # 처음 X 위치
        for c in range(N):
            if field[r][c] == "X":
                xr = r
                xc = c
            if field[r][c] == "Y":
                yr = r
                yc = c

    for C, com in command:
        cr, cc = xr, xc
        direction = 0
        for c in com:
            move(c)
        if cr == yr and cc == yc:
            result.append(1)
        else:
            result.append(0)

    print(f'#{tc}', *result)
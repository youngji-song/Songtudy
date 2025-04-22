# 2382 미생물 격리
'''
각 군집들은 1시간 마다 이동방향에 있는 다음 셀로 이동함
약품이 칠해진 셀에 도착하면 절반이 죽고 이동방향이 반대로 바뀜
    살아남은 미생물 = 원래 미생물 // 2
두 개 이상의 군집이 한 셀에 모이는 경우 합쳐짐
    합쳐진 미생물 = 군집들의 미생물 수의 합
    이동 방향: 미생물 수가 많은 군집의 이동방향

군집 정보: row, col, 미생물 수, 이동 방향 순
이동방향: 1: 상, 2: 하, 3: 좌, 4: 우
'''
import sys
sys.stdin = open('sample_input.txt','r')

def find(cells):
    global board
    board = [[[0,0] for _ in range(n)] for _ in range(n)]
    max_cnt_dict = {}
    new_cells = []
    for i in range(len(cells)):
        r, c, cnt, dir = cells[i]

        if dir == 1:
            if r == 1:
                cnt //= 2
                dir = 2
            if board[r-1][c][0]:
                board[r-1][c][0] += cnt
                if cnt > max_cnt_dict[(r-1, c)][0]:
                    board[r-1][c][1] = dir
                    max_cnt_dict[(r-1, c)] = (cnt, dir)
            else:
                board[r-1][c] = [cnt, dir]
                max_cnt_dict[(r-1,c)] = (cnt, dir)
            continue

        if dir == 2:
            if r == n-2:
                cnt //= 2
                dir = 1
            if board[r+1][c][0]:
                board[r+1][c][0] += cnt
                if cnt > max_cnt_dict[(r+1, c)][0]:
                    board[r+1][c][1] = dir
                    max_cnt_dict[(r+1,c)] = (cnt, dir)
            else:
                board[r+1][c] = [cnt, dir]
                max_cnt_dict[(r+1,c)] = (cnt, dir)
            continue

        if dir == 3:
            if c == 1:
                cnt //= 2
                dir = 4
            if board[r][c-1][0]:
                board[r][c-1][0] += cnt
                if cnt > max_cnt_dict[(r, c-1)][0]:
                    board[r][c-1][1] = dir
                    max_cnt_dict[(r, c-1)] = (cnt, dir)
            else:
                board[r][c-1] = [cnt, dir]
                max_cnt_dict[(r,c-1)] = (cnt, dir)
            continue

        if dir == 4:
            if c == n-2:
                cnt //= 2
                dir = 3
            if board[r][c+1][0]:
                board[r][c+1][0] += cnt
                if cnt > max_cnt_dict[(r, c+1)][0]:
                    board[r][c+1][1] = dir
                    max_cnt_dict[(r, c+1)] = (cnt, dir)
            else:
                board[r][c+1] = [cnt, dir]
                max_cnt_dict[(r,c+1)] = (cnt, dir)
            continue

    for i in range(n):
        for j in range(n):
            if board[i][j][0]:
                new_cells.append([i, j, board[i][j][0], board[i][j][1]])

    return new_cells, board

# input -----------------------------------------------------------------------------
t = int(input())
for tc in range(1, t + 1):
    n, m, k = map(int, input().split())  # n: 셀의 개수, m: 격리 시간, k: 미생물 군집의 수

    cells = [list(map(int, input().split())) for _ in range(k)]

    for _ in range(m):
        cells, board = find(cells)

    ans = 0
    for i in range(n):
        for j in range(n):
            ans += board[i][j][0]

    print(f'#{tc}',ans)


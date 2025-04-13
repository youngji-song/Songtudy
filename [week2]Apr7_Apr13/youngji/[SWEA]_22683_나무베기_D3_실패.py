# 22683 나무 베기 D3
# 14:00 ~

'''
전진, 왼쪽으로 90도 회전, 오른쪽으로 90도 회전
n: n*n 필드, tree = 아빠가 벨 수 있는 최대 나무 수
G: 이동 가능
T: 나무, 이동 불가
X: 출발지
Y: 목적지

항상 위쪽을 바라보는 상태로 RC카 조작
'''
import sys
sys.stdin = open('sample_input.txt','r')

from collections import deque


def bfs(field):
    dirs = [0, 1, 2, 3]  # up, right, down, left

    # bfs
    q = deque()
    q.append((sr, sc, dirs[0], 0))
    visited = [[[1e9]*(max_cut + 1) for _ in range(n)] for _ in range(n)]
    visited[sr][sc][0] = 0

    drs = [-1, 0, 1, 0]
    dcs = [0, 1, 0, -1]

    # field_copy = []
    # for row in field:
    #     field_copy.append(row[:])

    while q:
        r, c, dir, cut = q.popleft()

        if field[r][c] == 'Y':
            min_cnt = min(visited[r][c])
            if min_cnt == 1e9:
                return -1
            return min_cnt

        for d in range(4):
            nr, nc = r + drs[d], c + dcs[d]

            if 0 > nr or nr >= n or 0 > nc or nc >= n:
                continue

            if field[nr][nc] in ('G', 'Y'):
                # 이전과 같은 방향
                if abs(dir-d)==0:
                    if visited[nr][nc][cut] > visited[r][c][cut] + 1:
                        visited[nr][nc][cut] = visited[r][c][cut] + 1
                        q.append((nr, nc, d, cut))
                # 한 번 회전
                elif abs(dir - d) != 2:
                    if visited[nr][nc][cut] > visited[r][c][cut] + 2:
                        visited[nr][nc][cut] = visited[r][c][cut] + 2
                        q.append((nr, nc, d, cut))
                # 두 번 회전
                elif abs(dir - d) == 2:
                    if visited[nr][nc][cut] > visited[r][c][cut] + 3:
                        visited[nr][nc][cut] = visited[r][c][cut] + 3
                        q.append((nr, nc, d, cut))

            elif field[nr][nc] == 'T' and cut < max_cut:
                # 이전과 같은 방향
                if abs(dir-d)==0:
                    if visited[nr][nc][cut+1] > visited[r][c][cut] + 1:
                        visited[nr][nc][cut+1] = visited[r][c][cut] + 1
                        q.append((nr, nc, d, cut+1))
                # 한 번 회전
                elif abs(dir - d) != 2:
                    if visited[nr][nc][cut+1] > visited[r][c][cut] + 2:
                        visited[nr][nc][cut+1] = visited[r][c][cut] + 2
                        q.append((nr, nc, d, cut+1))

    return -1

t = int(input())
for tc in range(1, t+1):
    n, max_cut = map(int, input().split())
    field = [list(map(str, input().strip())) for _ in range(n)]


    sr, sc = 0, 0   # start_row, start_col
    for i in range(n):
        for j in range(n):
            if field[i][j] == 'X':
                sr, sc = i, j
                break

    ans = bfs(field)

    print(f'#{tc}',ans)
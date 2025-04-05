# 14502 연구소 Gold IV
# 15:42 ~ 17: 30

'''
0: 빈 칸
1: 벽
2: 바이러스

안전 영역: 바이러스가 퍼질 수 없는 곳 (1은 제외)
벽 3개를 세운 뒤 안전영역의 최댓값

1. 0 인 곳 중에서 3개를 선택해서 벽을 세움
2. 바이러스가 벽을 만나지 않았다면 (0이랑 인접하면) 2로 바꿔줌 -> dfs
3. 남은 0의 개수 counting
'''
import sys
sys.stdin = open('input.txt','r')

# 조합 함수 (3개 뽑기)
def comb(cnt, idx):
    if cnt == 3:
        combs.append(temp[:])
        return combs
    
    for i in range(idx, len0):
        temp.append(i)
        comb(cnt+1, i+1)
        temp.pop()

from collections import deque

# input
n, m = map(int, input().split())
labs = [list(map(int, input().split())) for _ in range(n)]

# labs(지도)에서 0인 곳 중에서 3개 뽑기
# labs에서 0인 곳의 index
idx_0 = []
for i in range(n):
    for j in range(m):
        if labs[i][j] == 0:
            idx_0.append([i,j])
len0 = len(idx_0)

temp = []   # 각각의 조합 결과
combs = []  # 전체 조합 결과 목록
comb(0,0)

max_safe = 0    # 최댓값 0으로 초기화

for comb in combs:  # 각 조합 결과들에 대해서
    lab_copy = [row[:] for row in labs]     # deepcopy
    visited = [[False]*m for _ in range(n)] # bfs를 위한 visited

    for i in range(3):      # 벽 3개 세우기          
        lab_copy[idx_0[comb[i]][0]][idx_0[comb[i]][1]] = 1
    
    safe = 0    # 안전영역 개수
    q = deque() 
    
    for i in range(n):      # 바이러스 위치에서만 bfs 수행
        for j in range(m):
            if lab_copy[i][j] == 2:
                q.append([i, j])
    
    # bfs
    while q:
        r, c = q.pop()
        for dr, dc in [[0,1],[1,0],[0,-1],[-1,0]]:
            nr, nc = r + dr, c + dc
            if 0>nr or nr>=n or 0>nc or nc>=m:
                continue
            if lab_copy[nr][nc] == 1:
                continue
            if not visited[nr][nc]:
                q.append([nr, nc])
                visited[nr][nc] = True
                lab_copy[nr][nc] = 2

    # 안전영역 개수 세고 업데이트
    for i in range(n):
        for j in range(m):
            if lab_copy[i][j] == 0:
                safe  += 1
    max_safe = max(max_safe, safe)


print(max_safe)
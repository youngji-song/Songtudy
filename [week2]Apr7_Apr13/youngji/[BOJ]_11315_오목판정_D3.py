# 11315 오목 판정 D3
# 17:15 ~

import sys
sys.stdin = open('sample_input.txt','r')

'''
o: 돌이 있는 칸
.: 돌이 없는 칸

연속해서 n개의 돌이 있는 것을 찾으면 종료!
dfs 이용
'''
def dfs(r,c):
    global ans, count
    
    for dr, dc in [[0,1],[1,0],[0,-1],[-1,0],[1,1],[1,-1],[-1,1],[-1,-1]]:
        count = 1
        for k in range(1,5):  
            nr, nc = r + dr*k, c + dc*k
            
            # out of index
            if nr<0 or nr>=n or nc<0 or nc>=n:
                continue
            
            # 돌이 없는 칸
            if board[nr][nc] == '.':
                continue
            
            # 돌인경우
            elif board[nr][nc] == 'o': 
                count += 1
        
        # 연속해서 5개의 돌이 있는 경우
        if count == 5:
            ans = 'YES'
            return
                
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    board = [list(map(str, input().strip())) for _ in range(n)]
    
    ans = 'NO'
    for i in range(n):
        for j in range(n):
            if ans == 'YES':
                break
            
            elif board[i][j] == 'o':
                dfs(i,j)
                
    
    print(f'#{tc}', ans)

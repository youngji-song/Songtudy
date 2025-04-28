'''
def schedule(s):    # s는 시작 인덱스 
    global earn
    week = [False] * 7
    
    for i in range(s, N):
        T, P = counsel[i][0], counsel[i][1]
        if i+T <= N and not week[i]:
            earn += P
            for j in range(T):
                week[i+j] = True
        else:
            continue

N = int(input())
counsel = [list(map(int, input().split())) for _ in range(N)]
earn = 0

for i in range(N-1, 0, -1):
    if i + counsel[i][0] > N:
        continue
    elif i + counsel[i][0] <= N:
        last = i+1
        break

for s in range(last):
    schedule(s)

print(earn)
'''

import sys
input = sys.stdin.readline

N = int(input())
dp = [0]*(N+1)  #각 날짜의 최대 추익 저장

for i in range(1, N+1):
    T, P = map(int, input().split())
    dp[i] = max(dp[i-1], dp[i])
    if i+T <= N+1:
        dp[i+T-1] = max(dp[i-1]+P, dp[i+T-1])
        
print(dp[-1])
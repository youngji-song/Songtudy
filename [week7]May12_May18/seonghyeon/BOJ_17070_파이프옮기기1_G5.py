N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

# 3방향 표시를 위해 다차원 dp 사용 (다차원 visited 스타일)
dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1 # 초기 파이프 위치

for y in range(N):
    # 초기 파이프가 있으므로 연결하기 위해선 2부터 시작해야 함
    for x in range(2, N):
        if board[y][x]: # board가 차있다면(벽)
            continue
        
        # 가로 (0)
        if not board[y][x] and not board[y][x-1]:
            # 각 그림에서 어떤 dp 값을 구해야하는 지 힌트가 있음!
            dp[y][x][0] = dp[y][x-1][0] + dp[y][x-1][2]

        # 세로 (1)
        if y > 0 and not board[y][x] and not board[y-1][x]:
            dp[y][x][1] = dp[y-1][x][1] + dp[y-1][x][2]


        # 대각 (2)
        if y > 0 and not board[y][x] and not board[y-1][x] and not board[y][x-1] and not board[y-1][x-1]:
            dp[y][x][2] = dp[y-1][x-1][0] + dp[y-1][x-1][1] + dp[y-1][x-1][2]

print(sum(dp[N-1][N-1]))
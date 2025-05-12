N = int(input())

# DP 배열 생성하기 (0부터 N까지 인덱스 사용하므로 N+1까지)
dp = [0]*(N+1)

# 2x1 타일을 채우는 방법
dp[1] = 1

# 2x2 타일을 채우는 방법 2*(1x2), 2*(2x1), (2x2)
if N >= 2:
    dp[2] = 3

# dp[n] = dp[n-1] + 2 * dp[n-2] 점화식
for i in range(3, N+1):
    dp[i] = (dp[i-1] + 2*dp[i-2]) % 10007

print(dp[N])
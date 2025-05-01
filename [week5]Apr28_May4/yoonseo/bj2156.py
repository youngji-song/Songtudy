N = int(input())
wine = [int(input()) for i in range(N)]
'''
dp = [-1] * N
def choice(s):
    answer = 0
    if s < N:
        return 0
    if dp[s] != -1:
        return dp[s]
    dp[s] = max(
        choice(s-1),
        choice(s-2)+wine[s]
        choice(s-3)+wine[s-1]+wine[s] if s>=2 else 0
    )
    return dp[s]

print(choice(N-1))
'''
dp = [0]*N

if N >= 1:
    dp[0] = wine[0]
if N >= 2:
    dp[1] = wine[0] + wine[1]
if N >= 3:
    dp[2] = max(dp[1], wine[0] + wine[2], wine[1] + wine[2])

for i in range(3, N):
    dp[i] = max(
        dp[i-1],
        dp[i-2] + wine[i],
        dp[i-3] + wine[i-1] + wine[i]
    )
print(dp[N-1])
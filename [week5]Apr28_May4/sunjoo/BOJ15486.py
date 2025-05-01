N = int(input())
lst = [(0, 0)]
l_idx = -1
for i in range(N):
    T, P = map(int, input().split())
    lst.append((T, P))
    if i+T <= N:
        l_idx = i+1

dp = [0] * (N+1)
dp[l_idx] = lst[l_idx][1]
m_idx = l_idx

for d in range(l_idx-1, 0, -1):
    dp[d] = max(dp[d+1], lst[d][1] + dp[d+lst[d][0]])
   
print(dp[1])
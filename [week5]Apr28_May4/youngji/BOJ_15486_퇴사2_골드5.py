n = int(input())
T, P = [0 for _ in range(n)], [0 for _ in range(n)]
for i in range(n):
    T[i], P[i] = map(int, input().split())

dp = [0] * (n+1)

for i in range(n-1,-1,-1):
    if i+T[i] <= n:
        dp[i] = max(P[i]+dp[i+T[i]], dp[i+1])
    else:
        dp[i] = dp[i+1]
print(dp[0])

'''
dp_time = [0 for _ in range(n)]
dp_pay = [0 for _ in range(n)]
for i in range(n-1,-1,-1):    # n일차부터 시작
    time = T[i]
    if time+i-1 >= n:    # 퇴사 전에 끝낼 수 없는 상담
        if i != n-1:
            dp_pay[i] = dp_pay[i+1]
        continue
    if dp_time[i:i+time] == [0]*time:    # 상담을 진행할 수 있는 경우 (t_i일동안 진행하는 상담이 없는경우)
        if i != n-1:
            dp_pay[i] = P[i] + dp_pay[i+1]
        else:
            dp_pay[i] = P[i]
        dp_time[i:i+time] = [i] * time
    else:
        if P[i] + dp_pay[i+time] > dp_pay[i+1]:   # 새로 진행하는 상담의 pay가 더 높은 경우
            dp_pay[i] = P[i] + dp_pay[i+time]
            dp_time[i:i+time] = [i] * time

print(dp_pay[0])
'''
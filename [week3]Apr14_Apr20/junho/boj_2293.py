def dp(price):
    global cnt
    if price == K:
        ans.sort()
        answer.add(tuple(ans))
        return
    for i in range(N):
        ans.append(coins[i])
        dp(price+coins[i])
        ans.pop()

N, K = map(int,input().split())
coins = [int(input()) for _ in range(N)]
ans = []
answer = set()
cnt = 0
dp(0)

print(answer)
print(len(answer))
N = int(input())
P = list(map(int, input().split()))
P = sorted(P)
ans = 0

for i in range(N):
    ans += P[i]*(N-i)

print(ans)
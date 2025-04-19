# 시간 초과
# N, K = map(int, input().split())
# degrees = list(map(int, input().split()))
# max_d = 0
#
# for d in range(0, N-K):
#     sum_d = sum(degrees[d:d+K])
#     max_d = max(max_d, sum_d)
#
# print(max_d)

N, K = map(int, input().split())
degrees = list(map(int, input().split()))
sum_d = sum(degrees[:K])
max_d = sum_d

for d in range(1, N-K+1):
    sum_d = sum_d - degrees[d-1] + degrees[d+K-1]
    max_d = max(max_d, sum_d)

print(max_d)
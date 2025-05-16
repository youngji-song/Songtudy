import sys
input = sys.stdin.readline


T = int(input())
for tc in range(T):

    N = int(input())
    rank = [list(map(int, input().split())) for _ in range(N)]

    rank.sort(key=lambda x:(x[0], x[1]))
    # print(rank)

    cnt = N
    best = N
    for i in range(N):
        if rank[i][1] <= best:
            best = rank[i][1]
            continue
        cnt -= 1
    print(cnt)
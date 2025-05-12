import sys
input = sys.stdin.readline

T = int(input())
for tc in range(T):
    N = int(input())
    candidate = [tuple(map(int, input().split())) for _ in range(N)]

    candidate.sort(key=lambda x: x[0])

    best = candidate[0][1]
    cnt = 1

    for i in range(1, N):
        if candidate[i][1] < best:
            cnt += 1
            best = candidate[i][1]
    
    print(cnt)
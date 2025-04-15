def sum_flies(i, j):
    flies = 0
    for r in range(i, i+M):
        flies += sum(arr[r][j:j+M])
    return flies


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_v = 0

    for i in range(N-M+1):
        for j in range(N-M+1):
            temp = sum_flies(i, j)
            max_v = max(temp, max_v)

    print(f'#{tc} {max_v}')
T = int(input())

for _ in range(T):
    N = int(input())
    apply = [tuple(map(int, input().split())) for _ in range(N)]

    # 방법1. 서류 기준 정렬
    apply.sort()
    cnt = 1 # 첫번째 지원자는 선발하고 시작하기
    min_v = apply[0][1] # 서류 기준 정렬이므로, 면접의 순위 비교

    for i in range(1, N):
        if apply[i][1] < min_v:
            cnt += 1
            min_v = apply[i][1]

    print(cnt)

###########################################################

    # 방법2. 면접 기준 정렬 (방법 2가 좀 더 빠름 큰 차이는 없음)
    apply.sort(key=lambda x: x[1])
    cnt = 1
    min_v = apply[0][0] # 면접 기준 정렬이므로, 서류의 순위 비교

    for i in range(1, N):
        if apply[i][0] < min_v:
            cnt += 1
            min_v = apply[i][0]

    print(cnt)
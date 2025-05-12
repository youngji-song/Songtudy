T = int(input())
for tc in range(1, T+1):
    N = int(input())
    scores = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    order_sorted = sorted(scores)
    order_sorted2 = sorted(scores, key=lambda x: x[1])
    lst_1 = []
    lst_2 = []

    for i in range(N):
        if order_sorted[0][1] > order_sorted[i][1]:
            lst_1.append(order_sorted[i])
        if order_sorted2[0][0] > order_sorted2[i][0]:
            lst_2.append(order_sorted2[i])

    # print(lst_1)
    # print(lst_2)
    # 교집합 구하기
    set_1 = set(tuple(item) for item in lst_1)
    set_2 = set(tuple(item) for item in lst_2)

    # 교집합
    intersection = set_1 & set_2

    # 다시 리스트로 변환
    common_items = [list(item) for item in intersection]

    print(len(common_items)+2)


    

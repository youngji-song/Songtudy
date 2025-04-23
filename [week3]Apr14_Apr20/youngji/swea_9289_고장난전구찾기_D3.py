t = int(input())
for tc in range(1, t+1):
    l, s = map(int, input().split())
    on_bulb = l // 2

    wrong_bulbs = {i for i in range(1,l+1)}
    for p in range(s):
        bulbs = list(map(int, input().split()))
        if sum(bulbs) < on_bulb:    # 하나가 안켜진 경우 -> 0 중에서 고르기
            wrong_bulbs = wrong_bulbs & {i+1 for i in range(l) if bulbs[i]==0 }
        elif sum(bulbs) > on_bulb:
            wrong_bulbs = wrong_bulbs & {i+1 for i in range(l) if bulbs[i]==1}

    print(f'#{tc}', *wrong_bulbs)
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(input().split())
    shuffle = []

    if N % 2 == 0:
        head = cards[:N//2]
        tail = cards[N//2:]
    else:
        head = cards[:N//2 + 1]
        tail = cards[N//2 + 1:]


    for i in range(N // 2 + 1):
        if i < len(head):
            shuffle.append(head[i])
        if i < len(tail):
            shuffle.append(tail[i])

    print(f'#{tc}', end=" ")
    print(*shuffle)
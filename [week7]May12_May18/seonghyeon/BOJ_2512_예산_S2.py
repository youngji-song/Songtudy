def binary(requests, total):
    left, right = 0, max(requests)
    res = 0

    while left <= right:
        middle = (left + right) // 2
        temp = sum(min(request, middle) for request in requests)

        if temp <= total:
            res = middle
            left = middle + 1
        
        else:
            right = middle - 1

    return res


N = int(input())
requests = list(map(int, input().split()))
M = int(input())

ans = binary(requests, M)

print(ans)
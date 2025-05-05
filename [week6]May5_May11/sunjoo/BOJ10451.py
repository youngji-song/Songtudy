T = int(input())
for tc in range(T):
    N = int(input())
    nums = [0] + list(map(int, input().split()))
    visited = [0] * (N+1)
    cnt = 0

    for i in range(1, N+1):
        now = i
        if visited[now]:
            continue
        while visited[now] == 0:
            visited[now] = 1
            now = nums[now]
        cnt += 1

    print(cnt)
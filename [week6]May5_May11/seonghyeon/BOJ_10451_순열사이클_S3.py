import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    visited = [False] * (N+1)
    print(visited)
    ans = 0
    for node in range(1, N+1):
        if visited[node]:
            continue
        # 자기 자신 순열 사이클
        if node == arr[node]:
            visited[node] = True
            ans +=1
            continue
        # 순열 사이클 생성
        cur_pos = node
        while not visited[cur_pos]:
            visited[cur_pos] = True
            cur_pos = arr[cur_pos]
        ans += 1
        
    print(ans)
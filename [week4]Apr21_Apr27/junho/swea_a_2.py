


def dijkstra(sr,sc,fuel):
    pq = [(fuel, sr,sc)]  # (누적거리, 노드번호)
    dists = [[INF] * N for _ in range(N)]     # 각 정점까지의 최단 거리를 저장할 리스트
    dists[sr][sc] = 0   # 시작노드 최단거리는 0

    while pq:
        f,r,c= heapq.heappop(pq)

        # 이미 더 작은 경로로 온 적이 있다면 pass
        # 예제 그림: c로 가는 경로가 3 or 4
        if dists[r][c] < f:
            continue

        for dir in range(4):
            nr = r + dr[dir]  # 다음 노드로 가기위한 가중치
            nc = c + dc[dir]  # 다음 노드 번호
            if nr < 0 or nr >= N or nc < 0 or nc >= N:
                continue
            # 다음 노드로 가기 위한 누적 거리
            if arr[r][c] > arr[nr][nc]:
                new_fuel = f + 0
            elif arr[r][c] == arr[nr][nc]:
                new_fuel = f + 1
            else:
                new_fuel = f + (arr[nr][nc]-arr[r][c])*2


        # 이미 같은 가중치거나, 더 작은 가중치로 온 적이 있디면 continue
            if dists[nr][nc] <= new_fuel:
                continue

            # next_node 까지 도착하는 데 비용은 new_dist
            dists[nr][nc] = new_fuel
            heapq.heappush(pq, (new_fuel,nr,nc))

    return dists

import heapq
INF = int(21e8)  # 21억 (무한대를 의미한다라고 가정)
dr = [-1,1,0,0]
dc = [0,0,-1,1]
T = int(input())
for tc in range(1,T+1):
    N = int(input())  # 노드수, 간선수 # 문제에 따라 다름
    arr = [list(map(int,input().split())) for _ in range(N)] # 인접 리스트로 구현

    result_dists = dijkstra(0,0,0)
    print(result_dists[N-1][N-1])

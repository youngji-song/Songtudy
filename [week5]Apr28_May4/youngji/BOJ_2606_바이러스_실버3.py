# 2606 바이러스 실버 3
# 22:42 ~ 22:55

'''
한 컴퓨터가 바이러스에 걸리면 네트워크상에서 연결된 모든 컴퓨터는 바이러스에 걸림
'''
from collections import defaultdict, deque

edge = int(input())    # 컴퓨터의 수
node = int(input())    # 네트워크 상에서 직접 연결되어있는 컴퓨터 쌍의 수

graph = defaultdict(list)
for i in range(node):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0 for _ in range(edge+1)]    # 0번째는 사용하지 않음
visited[1] = 1

starts = deque()
starts.append(1)
while starts:
    start = starts.popleft()
    for i in graph[start]:
        if not visited[i]:
            starts.append(i)
            visited[i] = 1

print(sum(visited)-1)
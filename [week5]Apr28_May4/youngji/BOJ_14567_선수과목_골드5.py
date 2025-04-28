# 14567 선수과목 골드5
# 23:30 ~ 24:10

'''
n: 과목 수, m: 선수 조건 수

a, b: a과목이 b과목의 선수 과목 a -> b
'''
from collections import defaultdict, deque

n, m = map(int, input().split())
graph = defaultdict(list)
values = [0 for _ in range(n+1)]    # 0번째 인덱스는 쓰지 않음!

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    values[b] += 1

subjects = [1 for _ in range(n+1)]  # 몇학기에 듣는지

q = deque()
for i in range(1,n+1):
    if values[i] == 0:
        q.append(i)

while q:
    pre = q.popleft()
    for i in graph[pre]:
        values[i] -= 1
        if values[i] == 0:
            q.append(i)
            subjects[i] = subjects[pre]+1

print(*subjects[1:])
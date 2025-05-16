# 1766 문제집 골드2
# 20:55 ~

'''
1~N번까지 총 N개의 문제 풀기
문제는 난이도 순서로 출제 (숫자가 작을수록 난이도가 낮음)

1. n개의 모든 문제를 풀어야 함
2. 먼저 푸는 것이 좋은 문제 -> 해당 문제를 먼저 풀어야 함
3. 가능하면 쉬운 문제부터 풀이

ex) 4 -> 2, 3 -> 1
'''
from collections import defaultdict

n, m = map(int, input().split())

graph = defaultdict(set)
for i in range(m):
    a, b = map(int, input().split())
    graph[b].add(a)

ans = []
for i in range(1,n+1):
    if len(graph[i]) == 0:
        ans.append(i)
    

'''
ans = [i for i in range(1,n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    if a < b:
        continue
    idx1 = ans.index(b)
    idx2 = ans.index(a)

    ans[idx1], ans[idx1+1:idx2+1], ans[idx2+1:] = a, ans[idx1:idx2], ans[idx2+1:]

print(*ans)
'''
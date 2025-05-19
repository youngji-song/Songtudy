import sys
input = sys.stdin.readline

N = int(input())
Ncard = list(map(int,input().split()))
M = int(input())
Mcard = list(map(int,input().split()))

cnt = {}
for i in Ncard:
    if i in cnt:
        cnt[i] += 1
    else:
        cnt[i] = 1

for j in Mcard:
    if j in cnt:
        print(cnt[j], end=' ')
    else:
        print(0, end=' ')
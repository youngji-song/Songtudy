N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A_sort = sorted(A)
B_sort = sorted(B)
S = 0
path = []

for b in B:
    idx = B_sort.index(b)
    more = path.count(b)
    idx += more
    path.append(b)
    S += b * A_sort[N-1-idx]

print(S)
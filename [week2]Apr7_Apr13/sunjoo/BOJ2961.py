def comb(cnt, path):

    if cnt == len(tastes):
        if path:
            result.append(path)
        return

    comb(cnt + 1, path)
    comb(cnt + 1, path + [cnt])
    return


def cook(lst):
    global min_v

    S = 1
    B = 0
    for l in lst:

        S *= tastes[l][0]
        B += tastes[l][1]

        min_v = min(abs(S-B), min_v)


N = int(input())
tastes = [list(map(int, input().split())) for _ in range(N)]
path = []
result = []
min_v = float('inf')


comb(0, [])

for r in result:
    cook(r)

print(min_v)
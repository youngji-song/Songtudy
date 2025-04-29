N = int(input())
counsel = [list(map(int, input().split())) for _ in range(N)]
def schedule(s):
    if s >= N:
        return 0
    result = 0
    if s + counsel[s][0] <= N:
        result = schedule(s + counsel[s][0]) + counsel[s][1]
    result = max(result, schedule(s+1))
    return result
print(schedule(0))
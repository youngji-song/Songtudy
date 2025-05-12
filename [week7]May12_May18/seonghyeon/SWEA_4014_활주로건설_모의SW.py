import sys
sys.stdin = open('input.txt', 'r')

def runway(line):
    visited = [False] * N

    for i in range(N-1):
        if line[i] == line[i+1]:
            continue
        # 오르막 경사로 체크
        if line[i] + 1 == line[i+1]:
            for j in range(i, i-X, -1):
                if j < 0 or line[j] != line[i] or visited[j]:
                    return False
                visited[j] = True
        # 내리막 경사로 체크
        elif line[i] - 1 == line[i+1]:
            for j in range(i+1, i+1+X):
                if j >= N or line[j] != line[i+1] or visited[j]:
                    return False
                visited[j] = True
        else:
            return False
    
    return True


T = int(input())

for tc in range(1, T+1):
    N, X = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    # 활주로 건설이 가능한 행&열을 확인해야 함

    # 행 검사
    for row in graph:
        if runway(row):
            cnt += 1 
    # 열 검사
    graph_t = list(zip(*graph))

    for col in graph_t:
        if runway(col):
            cnt += 1

    print(f'#{tc} {cnt}')
# 2819 격자판의 숫자 이어 붙이기 D4
# 20:35 ~ 20:55

'''
격자판이 주어졌을 때 만들 수 있는 서로 다른 일곱자리 수
'''

def dfs(i, j, number):
    global numbers
    if len(number) == 7:
        numbers.add(number)
        return numbers

    for dr, dc in [[0,1],[1,0],[0,-1],[-1,0]]:
        nr, nc = i + dr, j + dc
        if 0>nr or nr>=4 or 0>nc or nc>=4:
            continue
        dfs(nr, nc, number + board[nr][nc])


t = int(input())
for tc in range(1,t+1):
    board = [list(map(str, input().split())) for _ in range(4)]

    numbers = set()

    for i in range(4):
        for j in range(4):

            number = board[i][j]
            dfs(i, j, number)
    print(f'#{tc}',len(numbers))

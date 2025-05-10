def dfs(cnt, res, plus, minus, mul, div):
    global min_v, max_v

    # 중간/결과식 가지치기 (항상 -10억보다 크거나 같고, 10억보다 작거나 같다.)
    if not (int(-1e9)<=res<=int(1e9)):
        return

    if cnt == N:
        min_v = min(min_v, res)
        max_v = max(max_v, res)
        return
    
    # 연산자가 남아 있을 경우에만 해당 연산을 수행
    if plus:
        dfs(cnt+1, res+arr[cnt], plus-1, minus, mul, div)
    if minus:
        dfs(cnt+1, res-arr[cnt], plus, minus-1, mul, div)
    if mul:
        dfs(cnt+1, res*arr[cnt], plus, minus, mul-1, div)
    if div: # 음수 나눗셈을 고려해서 계산 필요함
        dfs(cnt+1, int(res/arr[cnt]), plus, minus, mul, div-1)

N = int(input())
arr = list(map(int, input().split()))

plus, minus, mul, div = map(int, input().split())

min_v = float('inf')
max_v = float('-inf')

dfs(1, arr[0], plus, minus, mul, div)

print(max_v, min_v, sep='\n')
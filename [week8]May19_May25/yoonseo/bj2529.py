import sys
input = sys.stdin.readline

def get(a, b, arr):
    if arr == '<':
        if a > b:
            return False
    else:
        if a < b:
            return False
    return True

def back(cnt, num):
    if cnt==K+1:
        ans.append(num)
        return
    
    for i in range(10):
        if not visited[i]:
            if cnt == 0 or get(num[cnt-1], str(i), arr[cnt-1]):
                visited[i] = True
                back(cnt+1, num+str(i))
                visited[i] = False


K = int(input())
arr = list(input().split())
visited = [False]*10
ans = []
back(0, '')

ans.sort()
print(ans[-1])
print(ans[0])
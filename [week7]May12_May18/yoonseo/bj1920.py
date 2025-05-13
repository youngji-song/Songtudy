import sys
input = sys.stdin.readline

N = int(input())
arr = set(map(int, input().split()))
M = int(input())
num = list(map(int, input().split()))

for i in num:
    print(1) if i in arr else print(0)
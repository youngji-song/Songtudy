T = int(input())
for tc in range(1, T+1):
    assign = list(input())
    stack = []
    lasers = []
    cnt = 0
    for i, a in enumerate(assign):
        if a == '(':
            stack.append((i, a))
            lasers.append(0)
        else:
            if stack and stack[-1][0] == i-1:   # stack 의 top '(' 가 직전 것 일 경우 레이저
                stack.pop()
                lasers.pop()
                if lasers:
                    for idx in range(len(lasers)):
                        lasers[idx] += 1
            else:
                stack.pop()
                cnt += (lasers.pop() + 1)

    print(f'#{tc} {cnt}')
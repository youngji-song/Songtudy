N, M = map(int, input().split())
chess = [list(input()) for _ in range(N)]
cnt = []

for i in range(N-7):
    for j in range(M-7):
        w_idx = 0
        b_idx = 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b)%2==0:
                    if chess[a][b]!='W':
                        w_idx+=1
                    else:
                        b_idx+=1
                else:
                    if chess[a][b]!='w':
                        b_idx+=1
                    else:
                        w_idx+=1
        cnt.append(w_idx)
        cnt.append(b_idx)
print(min(cnt))
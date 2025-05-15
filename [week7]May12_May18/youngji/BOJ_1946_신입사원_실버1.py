# 1946 신입사원 Silver1
# 17:05 ~
# 그리디..? dp로 풀었음 ㅠ

'''
다른 모든 지원자와 비교했을 때
    '서류심사 성적'과 '면접시험 성적' 중
    적어도 하나가 다른 지원자보다 떨어지지 않는 자만 선발
    -> 하나라도 높으면 선발 가능
    -> 서류/ 면접 중 1위가 있으면 선발 가능!

    -> (서류 순위 1등의 면접 순위)와 (면접 순위 1등의 서류 순위) 사이 값!

선발할 수 있는 신입사원의 최대 인원수?

서류심자 성적, 면접 성적의 '순위'가 주어짐
숫자가 작아야 선발됨!

'''

t = int(input())
for tc in range(1,t+1):
    n = int(input())

    scores = []
    for i in range(n):
        s1, s2 = map(int,input().split())
        scores.append((s1, s2))

    scores = sorted(scores)
    dp = [scores[0][1]]

    for i in range(n):
        if scores[i][1] < dp[-1]:
            dp.append(scores[i][1])

    print(len(dp))

    '''for i in range(n):
        if scores[i][0] == 1:
            bd1 = scores[i][1]
        elif scores[i][1] == 1:
            bd2 = scores[i][0]

    cnt = 0
    ans = []
    for i in range(n):
        if scores[i][0] < bd2 and scores[i][1] < bd1:
            cnt += 1
            ans.append(scores[i])

    # print(scores)
    # print(bd1, bd2)
    print(cnt+2)
    # print(ans)'''

    '''scores.sort(key=lambda x:(x[1],x[0]))
    print(scores)
    for i in range(n):
        if scores[i][1] > bd1:
            result = i
            break
        
    print(bd1)
    print(result)
'''


    '''# 순위 중 하나라도 1등이 있으면
        # 정렬을 했을 때 서류 1등은 무조건 합격?
    scores = sorted(scores)
    # print(scores)

    new = []    # 뽑힌 신입사원의 점수의 순위
    new.append(scores[0])

    for i in range(1,n):
        if scores[i][1] < scores[0][1]:
            new.append(scores[i])

    m = len(new)
    cnt = 0
    for i in range(m):
        cnt += 1
        if new[i][1] == 1:
            break

    print(cnt)'''


    '''
    # scores1: 서류 심사 성적 순위
    # scores2: 면접 심사 성적 순위
    scores1, scores2 = [0 for _ in range(n)], [0 for _ in range(n)]
    for i in range(n):
        s1, s2 = map(int, input().split())
        scores1[i], scores2[i] = s1, s2

    for i in range(n-1):
        # i번째 사람의 순위가 더 낮을 때 
        if (scores1[i] < scores1[i+1]) and (scores2[i] < scores2[i+1]):
            # (i+1)번째 사람은 선발될 수 없음
            '''


# 적어도 하나는 다른 지원자보다 높음
# 시험성적을 정렬 하고 다음에 면접성적 확인 
# -> 시험과 면접 둘다 낮은 사람 cnt 안함
# 리스트 형태로 넣어주고 소트 돌리기 첫번째 기준이니까
# 그리고 시험성적 기준으로 면접 성적 낮은 애들 확인

t = int(input())
for tc in range(1,t+1):
    n = int(input())
    people = []
    cnt = 0


    for _ in range(n):
        s_test, m_test = map(int, input().split())
        people.append([s_test, m_test])

    people.sort()
    min_num = people[0][1]
    cnt += 1

    for i in range(1,n):
        if people[i][1] < min_num:
            cnt += 1
            min_num = people[i][1]
        else:
            continue
    
    print(cnt)
        

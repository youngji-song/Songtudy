from collections import defaultdict, Counter

def solution(points, routes):
    # defaultdict 자료형을 써서 없는 키에 접근해도 자동으로 빈 리스트 생성
    timeline = defaultdict(list)
    total = 0

    for path in routes:
        t = 0
        for i in range(1, len(path)):
            x, y = points[path[i - 1] - 1]
            tx, ty = points[path[i] - 1]

            if i == 1:
                timeline[t].append((x, y))

            while x != tx:
                if x < tx:
                    x += 1
                else:
                    x -= 1
                t += 1
                timeline[t].append((x, y))

            while y != ty:
                if y < ty:
                    y += 1
                else:
                    y -= 1
                t += 1
                timeline[t].append((x, y))

    for step in timeline:
        coord_cnt = Counter(timeline[step]) # 반복 가능한 자료형에서 요소의 개수를 세주는 특수한 딕셔너리
        for cnt in coord_cnt.values():
            if cnt > 1:
                total += 1

    return total
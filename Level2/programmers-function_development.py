# 프로그래머스 기능개발
def solution(progresses, speeds):
    answer = []
    cnt = 0
    while progresses:
        if progresses[0] + speeds[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        else:
            if cnt > 0:
                answer.append(cnt)
                cnt = 0
            else:
                for i in range(len(progresses)):
                    progresses[i] += speeds[i]

    answer.append(cnt)

    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
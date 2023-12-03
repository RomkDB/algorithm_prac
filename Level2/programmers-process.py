# 프로그래머스 프로세스
def solution(priorities, location):
    answer = 0
    max_idx = priorities.index(max(priorities))

    while True:
        max_value = max(priorities)

        if priorities[max_idx] == max_value:
            priorities[max_idx] = 0
            answer += 1

            if max_idx == location:
                break

        max_idx += 1

        if max_idx >= len(priorities):
            max_idx = 0

    return answer

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))
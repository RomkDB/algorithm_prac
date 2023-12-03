# 프로그래머스 가장 큰 수
def solution(numbers):
    answer = ''
    str_num = []

    for i in numbers:
        str_num.append(str(i))

    str_num.sort(key=lambda x:x*3, reverse=True)

    # int로 변환하는 이유는 모든 원소가 0일 경우 0으로 만들기 위해서
    answer = str(int(''.join(str_num)))

    return answer

print(solution([6, 10, 2]))
# print(solution([0, 0, 0]))
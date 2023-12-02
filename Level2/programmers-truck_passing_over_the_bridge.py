# 프로그래머스 다리를 지나는 트럭
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    cnt = 0
    current_weight = 0
    dq = deque([0] * bridge_length)

    while dq:
        current_weight -= dq.popleft()
        answer += 1

        if truck_weights:
            if current_weight + truck_weights[0] <= weight:
                truck = truck_weights.pop(0)
                dq.append(truck)
                current_weight += truck
            else:
                dq.append(0)

    return answer

print(solution(2, 10, [7,4,5,6]))
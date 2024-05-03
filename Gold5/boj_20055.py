# 백준 20055번 컨베이어 벨트 위의 로봇
from collections import deque

n, k = map(int, input().split())
belt_line = deque(list(map(int, input().split())))
robot_line = deque([False] * n)
result = 1

while True:
    belt_line.rotate()
    robot_line.rotate()
    robot_line[n-1] = False

    for i in range(n-2, -1, -1):
        if robot_line[i] and not robot_line[i+1] and belt_line[i+1] >= 1:
            robot_line[i] = False
            robot_line[i+1] = True
            belt_line[i+1] -= 1
    
    robot_line[n-1] = False

    if belt_line[0] >= 1:
        robot_line[0] = True
        belt_line[0] -= 1

    if belt_line.count(0) >= k:
        break
    
    result += 1

print(result)

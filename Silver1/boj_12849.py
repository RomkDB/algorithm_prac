# 백준 12849번 본대 산책
d = int(input())
dp = [1, 0, 0, 0, 0, 0, 0, 0]

def move_case(position):
    tmp = [0 for _ in range(8)]
    tmp[0] = position[1] + position[2]
    tmp[1] = position[0] + position[2] + position[3]
    tmp[2] = position[0] + position[1] + position[3] + position[4]
    tmp[3] = position[1] + position[2] + position[4] + position[5]
    tmp[4] = position[2] + position[3] + position[5] + position[7]
    tmp[5] = position[3] + position[4] + position[6]
    tmp[6] = position[5] + position[7]
    tmp[7] = position[4] + position[6]

    for i in range(8):
        tmp[i] %= 1000000007
    
    return tmp
    
for i in range(d):
    dp = move_case(dp)

print(dp[0])
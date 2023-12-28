# 백준 돌 게임
n = int(input())
game = [-1] * 10001
game[1] = 1
game[2] = 0
game[3] = 1

for i in range(4, n+1):
    if game[i-1] == 1 or game[i-3] == 1:
        game[i] = 0
    else:
        game[i] = 1

if game[n] == 1:
    print('SK')
else:
    print('CY')
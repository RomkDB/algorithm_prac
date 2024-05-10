# 백준 2920 음계
line = list(map(int, input().split()))
asc = True
desc = True

for i in range(1, 8):
    # 앞의 수보다 큰 경우 -> 내림차가 아님
    if line[i] > line[i - 1]:
        desc = False
    # 앞의 수보다 작은 경우 -> 오름차가 아님
    elif line[i] < line[i - 1]:
        asc = False

if asc:
    print('ascending')
elif desc:
    print('descending')
else:
    print('mixed')

# 다른 풀이
# line = list(map(int, input().split()))

# if line == sorted(line):
#     print('asceding')
# elif line == sorted(line, reverse=True):
#     print('descending')
# else:
#     print('mixed')
# 백준 2920 음계
line = list(map(int, input().split()))
asc = True
desc = True

for i in range(1, 8):
    if line[i] > line[i - 1]:
        desc = False
    elif line[i] < line[i - 1]:
        asc = False

if asc:
    print('ascending')
elif desc:
    print('descending')
else:
    print('mixed')
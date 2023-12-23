# 백준 세로읽기
s_list = []
total = ''
max_len = 0

for _ in range(5):
    s = input()
    s_list.append(s)
    if max_len < len(s):
        max_len = len(s)

for i in range(max_len):
    for j in range(5):
        if i < len(s_list[j]):
            total += s_list[j][i]

print(total)

# s[0][0] + s[1][0] + s[2][0] + s[3][0] + s[4][0] + s[0][1] + .....
# 00 / 10 / 20 / 30 / 40
# 01 / *11 / 21 / 31 / 41
# 02 / *12 / 22 / 32 / 42
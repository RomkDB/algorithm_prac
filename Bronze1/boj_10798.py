# # 백준 세로읽기
s_list = []
result = ''
max_len = 0

for _ in range(5):
    s = input()
    s_list.append(s)
    # 단어의 최대 길이로 업데이트
    if max_len < len(s):
        max_len = len(s)

# i : 열, j : 행(5로 고정)
for i in range(max_len):
    for j in range(5):
        # i열의 글자를 세로로 탐색할 때
        # 행(j)마다 단어의 길이가 탐색하는 열(i)보다 큰 경우에만
        # 글자가 존재하기 때문에
        if i < len(s_list[j]):
            result += s_list[j][i]

print(result)

# # s[0][0] + s[1][0] + s[2][0] + s[3][0] + s[4][0] + s[0][1] + .....
# # 00 / 10 / 20 / 30 / 40
# # 01 / *11 / 21 / 31 / 41
# # 02 / *12 / 22 / 32 / 42
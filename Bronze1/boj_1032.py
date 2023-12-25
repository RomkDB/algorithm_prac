# 백준 명령 프롬프트
search_list = []
n = int(input())

for _ in range(n):
    s = input()
    search_list.append(s)

first_word = list(search_list[0])
# [c,o,n,f,i,g,?,?,?,?]
for i in range(1,n):
    for j in range(len(first_word)):
        if first_word[j] == search_list[i][j]:
            continue
        else:
            first_word[j] = '?'

print(''.join(first_word))
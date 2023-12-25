# 백준 단어 공부
s = input()
s = s.upper()
use_word = list(set(s))

cnt_list = []
for i in use_word:
    cnt = s.count(i)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list)) > 1:
    print('?')
else:
    many_word = cnt_list.index(max(cnt_list))
    print(use_word[many_word])
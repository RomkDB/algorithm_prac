# 백준 단어 공부
from collections import Counter

s = input().upper()
# 상위 빈도수 2개
s_count = Counter(s).most_common(2)

# s_count가 2개인 경우 두 글자의 빈도수가 같은지 비교
if len(s_count) > 1 and s_count[0][1] == s_count[1][1]:
    print('?')
else:
    print(s_count[0][0])
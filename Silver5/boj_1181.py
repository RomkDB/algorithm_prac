# 단어 정렬
n = int(input())
s_list = []

for _ in range(n):
    s_list.append(input())

s_list = list(set(s_list))
s_list.sort()
s_list.sort(key = lambda x : len(x))

for w in s_list:
    print(w)
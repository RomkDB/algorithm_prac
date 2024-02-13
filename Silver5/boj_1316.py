# 백준 그룹 단어 체커
n = int(input())
result = 0

for _ in range(n):
    s = input()
    char_set = set()
    is_group = True
    prev_char = ''

    for i in s:
        if i in char_set and i != prev_char:
            is_group = False
            break
        char_set.add(i)
        prev_char = i

    if is_group:
        result += 1

print(result)
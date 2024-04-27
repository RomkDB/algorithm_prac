# 백준 2812번 크게 만들기
n, k = map(int, input().split())
s_num = input()
rm_cnt = 0
stack = []

for i in s_num:
    while len(stack) > 0 and stack[-1] < i:
        if rm_cnt == k:
            break
        else:
            stack.pop()
            rm_cnt += 1
    stack.append(i)

for j in range(k - rm_cnt):
    stack.pop()

print(''.join(stack))
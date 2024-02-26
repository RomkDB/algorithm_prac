# 백준 괄호의 값
s = input()
stack = []
temp = 1
pre = ''
answer = 0

for i in s:
    if i == '(':
        temp *= 2
        stack.append(i)
    elif i == '[':
        temp *= 3
        stack.append(i)
    elif i == ')':
        if not stack or stack[-1] == '[':
            answer = 0
            break
        if pre == '(':
            answer += temp
        temp //= 2
        stack.pop()
    elif i == ']':
        if not stack or stack[-1] == '(':
            answer = 0
            break
        if pre == '[':
            answer += temp
        temp //= 3
        stack.pop()
    pre = i

if stack:
    answer = 0
print(answer)
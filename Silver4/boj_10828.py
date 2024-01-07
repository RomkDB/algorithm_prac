# 백준 스택
import sys

n = int(sys.stdin.readline())
stack = []

for _ in range(n):
    fun = sys.stdin.readline().split()

    if fun[0] == 'push':
        stack.append(fun[1])
    elif fun[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif fun[0] == 'size':
        print(len(stack))
    elif fun[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif fun[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
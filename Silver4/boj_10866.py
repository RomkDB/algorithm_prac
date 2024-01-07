# 백준 덱
import sys
# n = int(input())
n = int(sys.stdin.readline())
deque = []

for _ in range(n):
    # fun = input().split()
    fun = sys.stdin.readline().split()

    if fun[0] == 'push_front':
        deque.insert(0, fun[1])
    elif fun[0] == 'push_back':
        deque.append(fun[1])
    elif fun[0] == 'pop_front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
            deque.pop(0)
    elif fun[0] == 'pop_back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque.pop())
    elif fun[0] == 'size':
        print(len(deque))
    elif fun[0] == 'empty':
        if len(deque) == 0:
            print(1)
        else:
            print(0)
    elif fun[0] == 'front':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[0])
    elif fun[0] == 'back':
        if len(deque) == 0:
            print(-1)
        else:
            print(deque[-1])
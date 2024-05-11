# 백준 17298번 오큰수
# input() 대신 sys.stdin.readline()을 사용하여 제출
n = int(input())
s_list = list(map(int, input().split()))
stack = []
nge = [-1] * n

for i in range(n):
    x = s_list[i]

    if len(stack) == 0 or stack[-1][0] >= x:
        stack.append((x, i))
    else:
        while len(stack) > 0:
            pre, idx = stack.pop()

            if pre >= x:
                stack.append((pre, idx))
                break
            else:
                nge[idx] = x
        
        stack.append((x, i))

print(*nge)
# 프로그래머스 큰 수 만들기
def solution(number, k):
    stack = []
    
    for i in number:
        while k > 0 and stack and stack[-1] < i:
            stack.pop()
            k -= 1
        stack.append(i)
        
    if k != 0:
        stack = stack[:-k]
        
    return ''.join(stack)

print(solution('1924', 2))
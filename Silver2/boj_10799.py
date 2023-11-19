# 백준 10799번 쇠막대기
lazer = input()
stack = []
cnt = 0

for i in range(len(lazer)):
    if lazer[i] == '(': # 쇠막대기의 시작점 = 쇠막대기 개수
        stack.append('(')
    else:
        if lazer[i-1] == '(':
            stack.pop()
            cnt += len(stack) # 이전에 들어온 쇠막대기 개수만큼 같이 절단되기 때문에
        else:
            stack.pop() 
            cnt += 1 # 끝에 절단된 하나만 추가

print(cnt)
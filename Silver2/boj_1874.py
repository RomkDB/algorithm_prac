# 백준 1874번 스택 수열
n = int(input())
cnt = 1
stack = []
op = []

for _ in range(n):
    num = int(input())

    # 입력된 숫자까지 stack에 오름차순으로 push
    while cnt <= num:
        stack.append(cnt)
        cnt += 1
        op.append('+')

    # stack의 마지막 숫자가 입력된 숫자와 같다면
    # stack에서 마지막 숫자를 제거하고
    # 연산자 '-'를 추가    
    if stack[-1] == num:
        stack.pop()
        op.append('-')
    # stack의 마지막 숫자가 입력된 숫자와 같지 않다면
    # 수열을 만들 수 없는 경우
    else:
        print('NO')
        exit(0)

for i in op:
    print(i)
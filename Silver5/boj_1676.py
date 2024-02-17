# 백준 팩토리얼 0의 개수
n = int(input())
answer = 0
f_num = 1

# n! 계산
for i in range(1, n+1):
    f_num *= i

# 계산된 n! 숫자를 뒤부터 0인지 검사
for j in str(f_num)[::-1]:
    if j == '0':
        answer += 1
    else:
        break

print(answer)
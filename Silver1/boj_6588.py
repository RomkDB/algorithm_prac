# 백준 골드바흐의 추축
# 입력.........시간초과
# import sys

# 소수 판별 리스트
prime_list = [False, False] + [True] * 999999

# 에라토스테네스의 체를 사용
for i in range(2, int(len(prime_list)**0.5)+1):
    if prime_list[i]:
        for j in range(i*2, 1000001, i):
            prime_list[j] = False

while True:
    # n = int(sys.stdin.readline())
    n = int(input())

    # 프로그램 종료 조건
    if n == 0:
        break

    # n-1부터 역순으로 3까지 
    for i in range(n-1, 2, -2):
        # n = a + b라면
        # 조건1 : i번째 숫자가 소수인지 판별(a)
        # 조건2 : b(n-i) 숫자가 소수인지 판별
        # i에 숫자가 내림차순으로 들어가기 때문에 b-a가 가장 큰 것을 먼저 출력함
        if prime_list[i] and prime_list[n-i]:
            print(f"{n} = {n-i} + {i}")
            break
    else:
        print('"Goldbach\'s conjecture is wrong."')
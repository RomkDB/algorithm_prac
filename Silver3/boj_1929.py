# 백준 소수 구하기
m, n = map(int, input().split())

# 0, 1은 소수가 아니기 때문에 고정으로 False
# 2~(n-1)까지는 True 설정
is_prime = [False, False] + [True] * (n-1)

# 2부터 n의 제곱근까지 반복(에라토스테네스의 체)
for i in range(2, int(n ** 0.5)+1):
    # i가 소수인 경우
    if is_prime[i]:
        # i의 배수는 소수가 아니기 때문에 False로 변경
        for j in range(i*2, n+1, i):
            is_prime[j] = False

for i in range(m, n+1):
    if is_prime[i]:
        print(i)
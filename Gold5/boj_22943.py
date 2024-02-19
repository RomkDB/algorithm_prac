# 백준 수
from itertools import permutations
k, m = map(int, input().split())
# k개를 뽑았을 때 만들 수 있는 최대 값
max_val = 10 ** k
# k개 뽑아서 만든 숫자를 저장
p_num = []
# p_num 중 조건1을 만족하는 숫자 저장
condition_set1 = set()
# p_num 중 조건2을 만족하는 숫자 저장
condition_set2 = set()

# 에라토스테네스의 체를 사용
prime_list = [False, False] + [True] * (max_val-1)

for i in range(2, int(len(prime_list)**0.5)+1):
    if prime_list[i]:
        for j in range(2*i, max_val, i):
            prime_list[j] = False

# k개를 뽑아 만들 수 있는 숫자
for c in permutations(range(10), k):
    # 첫번째자리에 0이 나오는 경우
    if c[0] == 0:
        continue
    num = int(''.join(list(map(str, c))))
    p_num.append(num)

# 조건1
for i in p_num:
    # 모든 수를 다 확인할 필요 없이
    # i의 절반만 확인하면 됨
    for j in range(2, (i+1)//2):
        if prime_list[j] and prime_list[i-j]:
            condition_set1.add(i)

# 조건2
def condition2(num, m):
    n = num
    # m으로 나누어 떨어지지 않을때까지 나눈 수
    while n % m == 0:
        n = n // m

    # 모든 수를 다 확인할 필요 없이
    # 제곱근까지만 확인하면 됨
    for i in range(2, int(n**0.5)+1):
        # n = a * b라면
        # 조건1 : n이 a의 배수인지(조건 3 인덱스 에러 해결방법)
        # 조건2 : a(i)가 소수인지
        # 조건3 : b(n//i)가 소수인지
        if n % i == 0 and prime_list[i] and prime_list[n // i]:
            return num

for i in p_num:
    condition_set2.add(condition2(i, m))

print(len(condition_set1 & condition_set2))
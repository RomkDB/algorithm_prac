# 백준 소수 & 팰린드롬
n = int(input())

# 팰린드롬 판별
def is_palin(n):
    if str(n) == str(n)[::-1]:
        return True
    return False

# 소수 판별
def is_prime(n):
    if n < 2:
        return False

    # 2 ~ n의 제곱근까지 확인
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

while True:
    if is_palin(n) and is_prime(n):
        print(n)
        break
    n += 1
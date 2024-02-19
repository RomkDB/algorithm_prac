# 백준 조합 0의 개수
# 조합 : {n \chose m} = n! / m!(n-m)!
n, m = map(int, input().split())

# num을 소인수분해 했을 때 2의 지수값을 구하는 함수
def exp2(num):
    # num이 2보다 작다면 2의 지수는 0
    if num < 2:
        return 0

    cnt = 0

    # 2의 지수값을 구하는 방식
    # 백준 1676번 방식과 동일함
    while num >= 2:
        cnt += num // 2
        num = num // 2

    return cnt

# num을 소인수분해 했을 때 5의 지수값을 구하는 함수
def exp5(num):
    if num < 5:
        return 0

    cnt = 0

    while num >= 5:
        cnt += num // 5
        num = num // 5

    return cnt

# 조합식에서 2의 지수값 : n! / m!(n-m)!
exp2_cnt = exp2(n) - exp2(m) - exp2(n-m)
# 조합식에서 5의 지수값 : n! / m!(n-m)!
exp5_cnt = exp5(n) - exp5(m) - exp5(n-m)
# 2 or 5의 지수값 중 더 작은 값을 출력
# why? 어떤 값을 소인수분해했을 때
# 2^4 * 3^2 * 5^2라고 한다면
# 2 1개와 5 1개가 곱해져야 0이 1개씩 생성됨
print(min(exp2_cnt, exp5_cnt))
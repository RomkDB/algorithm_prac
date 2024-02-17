# 백준 GCD 합
t = int(input())

# 유클리드 호제법
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

for _ in range(t):
    n_list = list(map(int, input().split()))
    answer = 0

    # 2중 반복문으로 모든 쌍의 최대공약수를 더함
    for i in range(1, len(n_list)):
        for j in range(i+1, len(n_list)):
            answer += gcd(n_list[i], n_list[j])

    print(answer)
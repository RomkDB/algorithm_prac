# 백준 최대공약수와 최소공배수
a, b = map(int, input().split())

# 최대공약수 : a를 b로 나누면서 나머지가 0이 될때까지
# 나머지를 b로, a를 b로 업데이트 함
# 수학적으로 a > b라는 조건이 있지만
# 코드상 b > a라도 2번째 반복에서 a > b 형태로 변경됨
# ex) a = 7, b = 15 =>(1회 반복 진행) a = b(15), b = a % b(7)
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

# 최소공배수 : a * b / 최대공약수
def lcm(a, b):
    return int(a * b / gcd(a, b))

print(gcd(a, b))
print(lcm(a, b))
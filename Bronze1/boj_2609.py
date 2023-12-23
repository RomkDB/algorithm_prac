# 최대공약수와 최소공배수
a, b = map(int, input().split())

def gcd(a, b):
    # if b > a:
    #     a, b = b, a
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return int(a * b / gcd(a, b))

print(gcd(a, b))
print(lcm(a, b))
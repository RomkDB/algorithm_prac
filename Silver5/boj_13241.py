# 백준 최소공배수
import math
a, b = map(int, input().split())
print(a*b//math.gcd(a,b))
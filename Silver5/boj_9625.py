# 백준 BABBA
k = int(input())
dp = [0 for _ in range(k+1)]
dp[0] = (1,0)
dp[1] = (0,1)

for i in range(2, k+1):
    a = dp[i-1]
    b = dp[i-2]
    dp[i] = (a[0]+b[0], a[1]+b[1])

print(dp[k][0], dp[k][1])

# k = int(input())
# a, b = 0, 1
# for i in range(1,k):
#     a, b = b, a+b
# print(a, b)
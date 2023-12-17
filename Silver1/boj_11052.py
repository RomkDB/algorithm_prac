# 백준 카드 구매하기
# dp[i] = 카드 1개 구매하는 최대가격
# p[k] = k개가 들어있는 카드팩의 가격
# 점화식 : dp[i] = p[k] + dp[i-k]
n = int(input())
pack = [0] + list(map(int, input().split()))
dp = [0 for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], pack[j] + dp[i-j])
        
print(dp[n])
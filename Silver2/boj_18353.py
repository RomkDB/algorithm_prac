# 백준 18353번 병사 배치하기
# LIS(Longest Increasing Subsequence) + reverse 문제
n = int(input())
soldiers = list(map(int, input().split()))
dp = [1] * n
soldiers.reverse()

for i in range(1, n):
    for j in range(i):
        if soldiers[j] < soldiers[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
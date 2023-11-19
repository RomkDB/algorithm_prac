# 백준 11053번 가장 긴 증가하는 부분 수열
# LIS(Longest Increasing Subsequence) 문제
a = int(input())
a_list = list(map(int, input().split()))
dp = [1] * a

for i in range(1, a): # 두번째부터 접근
    for j in range(i): # 첫번째부터 i 전까지
        if a_list[i] > a_list[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))
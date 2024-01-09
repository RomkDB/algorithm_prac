# 백준 수열
n = int(input())
n_list = list(map(int, input().split()))

asc_dp = [1] * n
desc_dp = [1] * n

for i in range(1, n):
    if n_list[i-1] <= n_list[i]:
        asc_dp[i] = asc_dp[i-1] + 1
    if n_list[i-1] >= n_list[i]:
        desc_dp[i] = desc_dp[i-1] + 1

print(max(max(asc_dp),max(desc_dp)))
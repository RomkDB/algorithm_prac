# 백준 11055번 가장 큰 증가하는 부분 수열
import copy

a = int(input())
seq_list = list(map(int, input().split()))
dp = copy.deepcopy(seq_list)

for i in range(1, a):
    for j in range(i):
        if seq_list[i] > seq_list[j]:
            dp[i] = max(seq_list[i] + dp[j], dp[i])

print(max(dp))
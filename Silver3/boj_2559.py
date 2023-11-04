# 백준 2559번 수열
n, k = map(int, input().split())
nums = list(map(int, input().split()))

answer = []
answer.append(sum(nums[:k]))

for i in range(n-k):
    answer.append(answer[i] - nums[i] + nums[k+i])

print(max(answer))
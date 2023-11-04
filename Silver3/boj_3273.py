# 백준 3273번 두 수의 합
n = int(input())
nums = sorted(list(map(int, input().split())))
x = int(input())
answer = 0
l, r = 0, n-1

while l < r:
    num_sum = nums[l] + nums[r]
    if num_sum == x:
        answer += 1
        l += 1
    elif num_sum < x:
        l += 1
    else:
        r -= 1
        
print(answer)
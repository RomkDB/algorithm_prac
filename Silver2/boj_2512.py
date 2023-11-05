# 백준 2512번 예산
n = int(input())
budgets = list(map(int, input().split()))
m = int(input())

low, high = 1, max(budgets)

while low <= high:
    sum_budget = 0
    mid = (low + high) // 2
    
    for i in range(n):
        if budgets[i] <= mid:
            sum_budget += budgets[i]
        else:
            sum_budget += mid
    
    if sum_budget <= m:
        low = mid + 1
    else:
        high = mid - 1
        
print(low - 1)
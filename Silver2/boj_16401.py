# 백준 16401 과자 나눠주기
m, n = map(int, input().split())
snacks = list(map(int, input().split()))
start = 1
end = max(snacks)
answer = 0

while start <= end:
    num = 0
    mid = (start + end) // 2
    
    for i in snacks:
        if i >= mid:
            num += i // mid
            
    if num >= m:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)
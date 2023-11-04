# 백준 2805번 나무 자르기
n, m = map(int, input().split())
heights = list(map(int, input().split()))

start = 1
end = max(heights)

while start <= end:
    sum_num = 0
    mid = (start + end) // 2

    for i in heights:
        if i >= mid:
            sum_num += i - mid

    if sum_num >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)
# 백준 1920 수 찾기
n = int(input())
n_list = list(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

n_list.sort()

for i in m_list:
    start, end = 0, n-1

    while start <= end:
        mid = (start + end) // 2
        if n_list[mid] == i:
            print(1)
            break
        elif n_list[mid] > i:
            end = mid - 1
        else:
            start = mid + 1
    else:
        print(0)
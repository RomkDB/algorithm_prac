# 백준 1920 수 찾기
# 이분 탐색
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

# 다른 풀이
# 해쉬 자료구조인 딕셔너리 사용
n = int(input())
n_list = set(map(int, input().split()))
m = int(input())
m_list = list(map(int, input().split()))

for i in m_list:
    if i not in n_list:
        print('0')
    else:
        print('1')
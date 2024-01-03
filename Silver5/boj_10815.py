# 백준 숫자 카드
# 이진탐색
n = int(input())
card_list = list(map(int,input().split()))
m = int(input())
dif_list = list(map(int,input().split()))

card_list.sort()

# -10 2 3 6 10

for i in dif_list:
    l, r = 0, n-1

    while l <= r:
        m = (l+r) // 2
        if card_list[m] == i:
            print(1, end=' ')
            break
        elif i < card_list[m]:
            r = m - 1
        else:
            l = m + 1
    else:
        print(0, end=' ')
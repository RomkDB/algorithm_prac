# 백준 부녀회장이 될테야
# 3층 1 / 5 / 15 / 35 / 70
# 2층 1 / 4 / 10 / 20 / 35
# 1층 1 / 3 / 6 / 10 / 15
# 0층 1 / 2 / 3 / 4 / 5

t = int(input())

for _ in range(t):
    k = int(input()) # 층
    n = int(input()) # 호
    mf = [f+1 for f in range(n)]
    for _ in range(k):
        for i in range(1, n):
            mf[i] += mf[i-1]
    print(mf[-1])
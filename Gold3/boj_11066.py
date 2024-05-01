# 백준 11066번 파일 합치기
# pypy3로 제출
t = int(input())

for _ in range(t):
    k = int(input())
    size = [0] + list(map(int, input().split()))
    final = [0 for _ in range(k+1)]
    dp = [[0 for i in range(k+1)] for _ in range(k+1)]

    for i in range(1, k+1):
        final[i] = final[i-1] + size[i]
    
    for i in range(2, k+1):
        for j in range(1, k+2-i):
            dp[j][j+i-1] = min([dp[j][j+n] + dp[j+n+1][j+i-1]
                                for n in range(i-1)]) + (final[j+i-1] - final[j-1])

    print(dp[1][k])
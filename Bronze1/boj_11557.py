# 백준 Yangjojang of The Year
t = int(input())
for _ in range(t):
    school = ''
    cnt = 0
    n = int(input())
    for i in range(n):
        s, a = input().split()
        if cnt < int(a):
            cnt = int(a)
            school = s
    print(school)
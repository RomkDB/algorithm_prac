# 백준 스위치 켜고 끄기
n = int(input())
switch = [-1] + list(map(int, input().split()))
stu_num = int(input())
for _ in range(stu_num):
    stu = list(map(int, input().split()))
    if stu[0] == 1: # 남자
        for i in range(stu[1], n+1, stu[1]):
            if switch[i] == 1:
                switch[i] = 0
            elif switch[i] == 0:
                switch[i] = 1

    elif stu[0] == 2: # 여자
        center = stu[1]
        l, r = center - 1, center + 1
        if switch[center] == 1:
            switch[center] = 0
        elif switch[center] == 0:
            switch[center] = 1
        while l >= 0 and r <= n:
            if switch[l] == switch[r]:
                if switch[l] == 1:
                    switch[l] = 0
                    switch[r] = 0
                elif switch[l] == 0:
                    switch[l] = 1
                    switch[r] = 1
                l -= 1
                r += 1
            else:
                break

for i in range(1,len(switch)):
    print(switch[i], end=' ')
    if i % 20 == 0:
        print()
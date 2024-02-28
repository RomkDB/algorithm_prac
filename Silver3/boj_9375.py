# 백준 패션왕 신해빈
t = int(input())

for _ in range(t):
    n = int(input())
    costume_dic = {}

    for _ in range(n):
        part = input().split()
        if part[1] in costume_dic:
            costume_dic[part[1]].append(part[0])
        else:
            costume_dic[part[1]] = [part[0]]

    cnt = 1

    for i in costume_dic:
        cnt *= len(costume_dic[i]) + 1 # 해당 부위의 의상을 입지 않는 경우
        # ex. headgear 부위의 value가 [hat, turban]이라면
        # headhear 부위에 아무것도 장착 안하는 케이스를 더해서
        # 2가 아닌 3을 곱해야 함

    print(cnt - 1) # 알몸인 경우 제외


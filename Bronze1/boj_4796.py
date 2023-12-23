# 백준 캠핑
cnt = 0
while True:
    cnt += 1
    l, p, v = map(int, input().split())

    if l == 0 and p == 0 and v == 0:
        break
    day = v // p
    dont = v % p
    if l < dont:
        dont = l

    print("Case %d: %d" % (cnt, day*l+dont))
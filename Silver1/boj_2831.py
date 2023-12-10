# 외계인의 기타 연주
# 백준에서는 sys.stdin.readline()으로 입력
n, p = map(int, input().split())
line = [[0] for x in range(7)]
cnt = 0

for i in range(n):
    line_num, plat_num = map(int, input().split())

    while line[line_num][-1] > plat_num:
        line[line_num].pop()
        cnt += 1

    if line[line_num][-1] == plat_num:
        continue

    line[line_num].append(plat_num)
    cnt += 1

print(cnt)
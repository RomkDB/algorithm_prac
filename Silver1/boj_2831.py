# 외계인의 기타 연주
# 백준에서는 sys.stdin.readline()으로 입력
n, p = map(int, input().split())
line = [[0] for x in range(7)]
cnt = 0

for _ in range(n):
    line_num, plat_num = map(int, input().split())

    # 현재 줄에 누른 플렛이 입력 받은 플렛보다 높은 경우
    # -> 더 낮은 플렛이 입력으로 들어올 때까지 손가락을 떼면서 횟수 증가
    while line[line_num][-1] > plat_num:
        line[line_num].pop()
        cnt += 1

    # 이미 누르고 있는 경우
    if line[line_num][-1] == plat_num:
        continue

    # 새로운 줄의 플렛을 누름
    line[line_num].append(plat_num)
    cnt += 1

print(cnt)
# 백준 2007년
week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
md = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
x, y = map(int, input().split())
days = 0

for i in range(x):
    if x == i+1:
        days += y
    else:
        days += md[i]

print(week[days%7-1])
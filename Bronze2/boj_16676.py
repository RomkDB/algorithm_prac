# 백준 16676번 근우의 다이어리 꾸미기
n = input()
s_dummy = '1' * len(n)

if len(n) == 1:
    print(1)
elif int(n) >= int(s_dummy):
    print(len(n))
else:
    print(len(n) - 1)
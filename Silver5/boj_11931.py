# 수 정렬하기 4
import sys

n = int(sys.stdin.readline())
n_list = []

for _ in range(n):
    n_list.append(int(sys.stdin.readline()))

n_list.sort(reverse=True)
for i in n_list:
    print(i)
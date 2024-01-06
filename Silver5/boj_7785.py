# 백준 회사에 있는 사람
# 리스트보다 딕셔너리가 해쉬맵 자료구조 형태라 추가&삭제 연산이 빠름
import sys

n = int(sys.stdin.readline())
p_dic = {}

for _ in range(n):
    name, s = sys.stdin.readline().rstrip().split()
    if s == 'enter':
        p_dic[name] = True
    elif s == 'leave':
        del p_dic[name]

p_list = sorted(p_dic.keys(), reverse=True)
for i in p_list:
    print(i)
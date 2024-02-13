# 백준 듣보잡
n, m = map(int, input().split())
nolisten = set()
nosee = set()

for _ in range(n):
    name = input()
    nolisten.add(name)

for _ in range(m):
    name = input()
    nosee.add(name)

nolistensee = sorted(list(nolisten & nosee))

print(len(nolistensee))
for i in nolistensee:
    print(i)
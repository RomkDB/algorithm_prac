# 백준 듣보잡
n, m = map(int, input().split())
nolisten = set() # 듣도 못한
nosee = set() # 보도 못한

# 2번째 줄부터 n개(듣도 못한)
for _ in range(n):
    name = input()
    nolisten.add(name)

# N+2번째 줄부터 m개(보도 못한)
for _ in range(m):
    name = input()
    nosee.add(name)

# 듣도 못합 집합과 보도 못한 집합의 교집합의 결과를 정렬(오름차순)
nolistensee = sorted(list(nolisten & nosee))

print(len(nolistensee))
for i in nolistensee:
    print(i)
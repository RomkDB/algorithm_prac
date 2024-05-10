# 백준 4195번 친구 네트워크
# Union Find 알고리즘
def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return parent[x]

def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        number[x] += number[y]

t = int(input())

for _ in range(t):
    parent = dict()
    number = dict()
    f_num = int(input())
    
    for _ in range(f_num):
        x, y = input().split()

        if x not in parent:
            parent[x] = x
            number[x] = 1
        if y not in parent:
            parent[y] = y
            number[y] = 1
        
        union(x, y)
    
        print(number[find(x)])
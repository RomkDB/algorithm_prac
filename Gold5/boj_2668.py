# 백준 숫자 고르기
n = int(input())
grid = [[] for _ in range(n+1)]
visited = [False] * (n+1)
answer = []

for i in range(n):
    num = int(input())
    grid[num].append(i+1)

def dfs(n, nodes):
    visited[n] = True
    nodes.add(n)
    for x in grid[n]:
        if x not in nodes:
            dfs(x, nodes.copy())
        else:
            answer.extend(list(nodes))
            return

for j in range(1, n+1):
    if not visited[j]:
        dfs(j, set([]))

answer.sort()
print(len(answer))
for k in answer:
    print(k)
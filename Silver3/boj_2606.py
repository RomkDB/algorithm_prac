# 백준 바이러스
n = int(input())
edge = int(input())
network = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 0

for _ in range(edge):
    x, y = map(int, input().split())
    network[x].append(y)
    network[y].append(x)
    
def dfs(root):
    global cnt
    cnt += 1
    visited[root] = True
    for next_node in network[root]:
        if not visited[next_node]:
            dfs(next_node)

dfs(1)
print(cnt-1)
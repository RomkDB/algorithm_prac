# 백준 DFS와 BFS
from collections import deque

def dfs(graph, v):
    visited = list()
    need_visit = list()
    
    need_visit.append(v)
    
    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(reversed(graph[node]))
    return visited

def bfs(graph, v):
    visited = list()
    need_visit = deque()
    
    need_visit.append(v)
    
    while need_visit:
        node = need_visit.popleft()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

for node in graph:
    node.sort()

print(*dfs(graph, v))
print(*bfs(graph, v))

# ------------------------------------------------
# dfs 재귀 사용
# from collections import deque

# def dfs(v):
#     print(v, end=" ")
#     visited[v] = True

#     for node in graph[v]:
#         if not(visited[node]):
#             dfs(node)

# def bfs(v):
#     need_visit = deque([v])
#     while need_visit:
#         node = need_visit.popleft()
#         if not visited[node]:
#             print(node, end=" ")
#             visited[node] = True
#             for i in graph[node]:
#                 if not visited[i]:
#                     need_visit.append(i)

# n, m, v = map(int, input().split())
# graph = [[] for _ in range(n+1)]

# for _ in range(m):
#     start, end = map(int, input().split())
#     graph[start].append(end)
#     graph[end].append(start)

# for node in graph:
#     node.sort()

# visited = [False] * (n+1)
# dfs(v)
# print()
# visited = [False] * (n+1)
# bfs(v)

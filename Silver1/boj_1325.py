# 백준 효율적인 해킹
n, m = map(int, input().split())
network = [[] for _ in range(n+1)]
answer = []
max_cnt = -1

for _ in range(m):
    a, b = map(int, input().split())
    network[b].append(a)
    
def dfs(start):
    visited = [False] * (n+1)
    need_visit = [start]
    visited[start] = True
    cnt = 0
    
    while need_visit:
        com = need_visit.pop()
        for i in network[com]:
            if not visited[i]:
                need_visit.append(i)
                visited[i] = True
                cnt +=1

    return cnt

for i in range(1, n+1):
    com = dfs(i)
    
    if com > max_cnt:
        answer = [i]
        max_cnt = com
    elif com == max_cnt:
        answer.append(i)
        max_cnt = com
        
print(*answer)
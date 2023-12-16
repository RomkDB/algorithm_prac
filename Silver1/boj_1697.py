# 백준 숨바꼭질
from collections import deque

n, k = map(int, input().split())
max_val = 100001
visited = [0] * max_val

def bfs():
    need_visit = deque([n])

    while need_visit:
        cur_node = need_visit.popleft()
        if cur_node == k:
            return visited[cur_node]
        for next_node in (cur_node-1, cur_node+1, cur_node*2):
            # 조건1 : 다음 이동할 노드는 0 ~ 100000 사이에 있어야 함
            # 조건2 : 다음 이동할 노드는 방문한 적이 없어야 함(0) => 중복노드 탐색 방지
            if 0 <= next_node < max_val and not visited[next_node]:
                # count 역할
                visited[next_node] = visited[cur_node] + 1
                need_visit.append(next_node)

print(bfs())
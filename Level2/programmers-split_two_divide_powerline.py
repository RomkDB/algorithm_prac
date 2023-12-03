# 프로그래머스 전력망을 둘로 나누기
from collections import deque

def bfs(start, graph, visited, check_link):
    dq = deque([start])
    visited[start] = True
    cnt = 1

    while dq:
        s = dq.popleft()

        for i in graph[s]:
            if visited[i] == False and check_link[start][i]:
                dq.append(i)
                visited[i] = True
                cnt += 1
    return cnt

def solution(n, wires):
    answer = n

    # 예시1 : 10 X 10
    check_link = [[True] * (n+1) for _ in range(n+1)]
    # 예시1 : [[], [], [], [], [], [], [], [], [], []]
    graph = [[] for _ in range(n+1)]

    # 예시1 : [[], [3], [3], [1, 2, 4], [3, 5, 6, 7], [4], [4], [4, 8, 9], [7], [7]]
    for i, j in wires:
        graph[i].append(j)
        graph[j].append(i)

    for x, y in wires:
        # 예시1 = [[False], [False], [False], [False], [False], [False], [False], [False], [False], [False]]
        visited = [False] * (n+1)
        # x -> y 선 차단
        check_link[x][y] = False
        # x 기준으로 연결된 송전탑 개수
        cnt_x = bfs(x, graph, visited, check_link)
        # y 기준으로 연결된 송전탑 개수
        cnt_y = bfs(y, graph, visited, check_link)
        # 차단한 선 초기화
        check_link[x][y] = True

        answer = min(answer, abs(cnt_x - cnt_y))

    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, [[1,2],[2,3],[3,4]]))
print(solution(7, [[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))
# 백준 15663번 N과 M(9)
n, m = map(int, input().split())
n_list = list(map(int, input().split()))
n_list.sort()
visit = [False] * n # 방문여부
temp = []

def df():
    if len(temp) == m:
        print(*temp)
        return
    
    prev_num = 0 # 이전에 선택한 숫자를 저장하는 변수
    
    for i in range(n):
        # 방문하지 않았고(not False -> True)
        # 이전에 선택한 숫자와 다르다면
        if not visit[i] and prev_num != n_list[i]:
            visit[i] = True # 방문처리
            temp.append(n_list[i])
            prev_num = n_list[i] # 이전에 선택한 숫자 업데이트 
            df() # 재귀 호출
            visit[i] = False # 재귀 호출이 끝나면 방문처리 초기화
            temp.pop() # 마지막으로 사용된 숫자 제거

df()
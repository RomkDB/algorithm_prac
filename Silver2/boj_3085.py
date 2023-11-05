# 백준 3085번 사탕 게임
n = int(input())
candies = [list(input()) for _ in range(n)]
cnt = 0

# 변경된 상태에서 행과 열을 확인하고 
# 연속된 사탕이 최대 개수를 리턴하는 함수
def check(candies, n):
    max_row = 1 # 행 기준 연속된 사탕의 최대 개수
    max_col = 1 # 열 기준 연속된 사탕의 최대 개수
        
    for i in range(n): # 행과 열 반복 탐색
        row_count = 1 # 현재 행에서 연속된 사탕의 개수로 사용할 변수
        
        for r in range(1, n): # 1부터인 이유는 2개씩 비교하기 때문에 n-1번 비교해야 함
            if candies[i][r-1] == candies[i][r]: # 좌우 비교
                row_count += 1
                max_row = max(max_row, row_count)
            # ★비교하다가 다른 사탕이 나오면 row_count를 1로 초기화 해야 함★
            # why? 그렇게 해야 끊어진 이후에 또 연속된 사탕의 개수를 1개부터 셀 수 있음
            else:
                row_count = 1
            
        col_count = 1 # 현재 열에서 연속된 사탕의 개수로 사용할 변수
        
        for c in range(1, n): # 1부터인 이유는 2개씩 비교하기 때문에 n-1번 비교해야 함
            if candies[c-1][i] == candies[c][i]: # 상하 비교
                col_count += 1
                max_col = max(max_col, col_count)
            # ★비교하다가 다른 사탕이 나오면 col_count를 1로 초기화 해야 함★
            # why? 그렇게 해야 끊어진 이후에 또 연속된 사탕의 개수를 1개부터 셀 수 있음
            else:
                col_count = 1
    
    return max(max_row, max_col) # 행 탐색 최대값과 열 탐색 최대값 중 큰 값

for x in range(n):
    for y in range(n):
        # 오른쪽, 아래 2가지만 변경하는 이유는 위, 왼쪽은 반복문 과정에서 중복됨
        if y+1 < n: # y의 범위는 0 ~ n-1
            # 오른쪽과 변경
            candies[x][y], candies[x][y+1] = candies[x][y+1], candies[x][y]
            # check 함수와 현재 최대값과 비교하여 최대값으로 변경
            cnt = max(cnt, check(candies, n))
            # 원상 복구
            candies[x][y], candies[x][y+1] = candies[x][y+1], candies[x][y]
        if x+1 < n: # x의 범위는 0 ~ n-1
            # 아래와 변경
            candies[x][y], candies[x+1][y] = candies[x+1][y], candies[x][y]
            # check 함수와 현재 최대값과 비교하여 최대값으로 변경
            cnt = max(cnt, check(candies, n))
            # 원상 복구
            candies[x][y], candies[x+1][y] = candies[x+1][y], candies[x][y]

print(cnt)
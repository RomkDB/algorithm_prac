# 백준 18111번 마인크래프트
# 백준에서 pypy3으로 제출하고 입력도 sys.stdin.readline을 사용
n, m, b = map(int, input().split())
field = [] # 입력받은 각 필드의 높이를 담기 위해
# 2차원 배열을 사용할 필요 없음
# why? 어짜피 정해진 영역에서 모든 높이를 비교하는 것이기 때문에
for _ in range(n):
    row = list(map(int, input().split()))
    field += row

min_time = float('inf') # 처음 구한 시간과 비교하기 위해 무한대로 초기값 설정
answer_height = 0 # 정답으로 구하고자 하는 높이로 사용하는 변수

for p_h in range(257): # 가능한 높이의 범위는 0 ~ 256
    total_time = 0 # 가능한 높이마다 작업 후 걸리는 시간을 담는 변수
    block_num = b # 처음 가지고 있던 블록의 수로 초기화
    
    for h in field:
        if h < p_h: # 블록을 추가하는 경우(기준으로 설정한 높이 - 각 필드의 높이)
            total_time += p_h - h
            block_num -= p_h - h
        elif h > p_h: # 블록을 제거하는 경우(각 필드의 높이 - 기준으로 설정한 높이)
            total_time += (h - p_h) * 2 # 블록 제거는 2초
            block_num += h - p_h
            
    # 1번 조건 : 블록의 수가 음수가 되면 안되고
    # 2번 조건 : 작업 후 걸린 시간이 다른 기준 높이의 작업 시간보다 작거나 같아야 함
    # 같을 때는 왜 갱신할까? 땅의 높이가 가장 높은 것을 출력해야 하기 때문에
    if block_num >= 0 and total_time <= min_time:
        min_time = total_time
        answer_height = p_h
            
print(min_time, answer_height)
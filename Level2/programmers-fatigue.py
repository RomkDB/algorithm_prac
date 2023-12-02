# 프로그래머스 피로도
from itertools import permutations

def solution(k, dungeons):
    case_list = []
    
    for case in permutations(dungeons, len(dungeons)):
        case_list.append(case)
        
    cnt_list = []
    for i in case_list:
        tired = k
        cnt = 0
        for j in i:
            if j[0] <= tired:
                tired -= j[1]
                cnt += 1
        
        cnt_list.append(cnt)
                
    return max(cnt_list)

print(solution(80, [[80,20],[50,40],[30,10]]))
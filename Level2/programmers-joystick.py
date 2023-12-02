# 프로그래머스 조이스틱
def solution(name):
    answer = 0
    move_cnt = len(name) - 1
    
    for i, spell in enumerate(name):
        answer += min(ord(spell) - ord('A'), ord('Z') - ord(spell) + 1)
        
        next = i + 1
        
        while next < len(name) and name[next] == 'A':
            next += 1
        
        move_cnt = min([move_cnt, 2 * i + len(name) - next, i + 2 * (len(name) - next)])
    
    answer += move_cnt
    
    return answer

print(solution('JEROEN'))
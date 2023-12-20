# 프로그래머스 카펫
def solution(brown, yellow):
    answer = []
    area = brown + yellow
    
    for w in range(3, brown):
        if area % w == 0:
            h = area / w
            if (w-2) * (h-2) == yellow:
                answer.append(w)
                answer.append(h)
                break
            
    answer.reverse()
    
    return answer
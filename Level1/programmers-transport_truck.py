# 프로그래머스 운송 트럭
def solution(max_weight, specs, names):
    answer = 0
    spec_dic = {}
    w = 0
    
    for i in specs:
        spec_dic[i[0]] = int(i[1])
        
    for j in names:
        if w + spec_dic[j] > max_weight:
            answer += 1
            w = spec_dic[j]
        else:
            w += spec_dic[j]
    return answer + 1

print(solution(300, [["toy","70"], ["snack", "200"]], ["toy", "snack", "snack"]))
print(solution(200, [["toy","70"], ["snack", "200"]], ["toy", "snack", "toy"]))
# 백준 염색체
t = int(input())
dna_kind1 = ['A', 'B', 'C', 'D', 'E', 'F']
dna_kind2 = ['A', 'F', 'C']

for _ in range(t):
    dna = input()
    answer = 'Infected!'

    # if dna[0] not in dna_kind1 or dna[-1] not in dna_kind1:
    if any(char not in dna_kind1 for char in dna):
        answer = 'Good'
    else:
        idx = 0
        pre = 'A'
        for i in dna[1:-1]:
            if pre != i:
                idx += 1
                if dna_kind2[idx] != i:
                    answer = 'Good'
                    break
            pre = i
    print(answer)

# AFCG 테스트 케이스에서는 오류가 발생함
# 첫번째 if문에서(line10) 2번째 조건이
# '그 다음에는 {A, B, C, D, E, F} 중 0개 또는 1개가 있으며, 더 이상의 문자는 없어야 한다.'
# 규칙의 더 이상 문자는 없어야 한다라는 부분을 정상적으로 처리하지 못함
# sol) if any(char not in dna_kind1 for char in dna):

# any() 함수 : 반복 가능한 변수에서 True가 1개라도 있으면 True 반환, 없다면 False 반환
# ex1) any([False, False, True]) => True
# ex2) any([False, False, False]) => False

# ==========================================
# # 정규표현식 사용
# import re

# t = int(input())
# # ^ : 패턴의 시작
# # ? : 패턴을 0번 또는 1번
# # $ : 패턴으로 끝남
# # + : 패턴이 1개 이상
# rule = re.compile('^[A-F]?A+F+C+[A-F]?$')

# for _ in range(t):
#     dna = input()

#     if rule.match(dna) == None:
#         print('Good')
#     else:
#         print('Infected')
# 백준 너의 평점은
score_dic = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0': 3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0}
sum = 0
cnt = 0
for _ in range(20):
    score = input().split()
    if score[2] != 'P':
        sum += float(score[1]) * score_dic[score[2]]
        cnt += float(score[1])
print('%.6f' % (sum/cnt))

# 다른 풀이
# score_dic = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0': 3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0}
# sum = 0
# cnt = 0
# for _ in range(20):
#     score = input().split()
#     if score[2] != 'P':
#         sum += float(score[1]) * score_dic[score[2]]
#         cnt += float(score[1])
# print(sum/cnt)
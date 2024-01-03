# 백준 점수 계산
score_list = []
sum = 0
idx = []

for i in range(8):
    score_list.append([i+1,int(input())])

score_list.sort(key=lambda x : x[1], reverse=True)

for j in range(5):
    sum += score_list[j][1]
    idx.append(score_list[j][0])

idx.sort()

print(sum)
print(*idx)
# 백준 1541 잃어버린 괄호
exp = input().split('-')
sum_num = 0

for i in exp[0].split('+'):
    sum_num += int(i)
    
for j in exp[1:]:
    for k in j.split('+'):
        sum_num -= int(k)
        
print(sum_num)
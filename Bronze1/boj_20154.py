# 백준 이 구역의 승자는 누구야?!
s_count = {'A':3, 'B':2, 'C':1, 'D':2, 'E':3, 'F':3, 'G':3,
           'H':3, 'I':1, 'J':1, 'K':3, 'L':1, 'M':3, 'N':3,
           'O':1, 'P':2, 'Q':2, 'R':2, 'S':1, 'T':2, 'U':1,
           'V':1, 'W':2, 'X':2, 'Y':2, 'Z':1}
s = input()
t_num = []

for i in s:
    t_num.append(s_count[i])

# 계속 더해서 1개가 남을 때까지 반복
while len(t_num) > 1:
    # 더한 숫자를 담아두는 리스트
    temp_list = []
    # 2개씩 짝을 지어 더해서 리스트에 저장
    for i in range(0, len(t_num)-1, 2):
        sum_num = t_num[i] + t_num[i+1]
        temp_list.append(sum_num % 10)
    # 짝이 이루어지지 않는 마지막 숫자가 있는 경우
    if len(t_num) % 2 == 1:
        temp_list.append(t_num[-1])
    # 더한 숫자를 담아두는 리스트를 다음 반복에 사용하기 위해
    t_num = temp_list

total = t_num[0]

# 그냥 다 더해서 10으로 나눈 나머지를 판별해도 된다...
# total = 0

# for i in s:
#     total += s_count[i]

if total % 2 == 1:
    print("I'm a winner!")
else:
    print("You're the winner?")
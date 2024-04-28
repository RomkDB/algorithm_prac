# 백준 5052번 전화번호 목록
# 입력을 sys.stdin.readline()으로 변경하여 제출
t = int(input())

for _ in range(t):
    n = int(input())
    num_list = []

    for i in range(n):
        phone_num = input().strip() # 공백제거
        num_list.append(phone_num)
    
    num_list.sort()
    result = False

    for j in range(n - 1):
        if len(num_list[j]) < len(num_list[j + 1]):
            if num_list[j] == num_list[j + 1][:len(num_list[j])]:
                result = True
                break
    
    if result:
        print("NO")
    else:
        print("YES")
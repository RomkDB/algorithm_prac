# 백준 5397번 키로거
test_case = int(input())

for _ in range(test_case):
    l = input()
    pw_list = []
    temp_list = []
    
    for i in l:
        if i == '<':
            if pw_list:
                temp_list.append(pw_list.pop())
        elif i == '>':
            if temp_list:
                pw_list.append(temp_list.pop())
        elif i == '-':
            if pw_list:
                pw_list.pop()
        else:
            pw_list.append(i)
    
    # temp에는 거꾸로 입력되었기 때문에
    pw_list.extend(reversed(temp_list))
    
    print(''.join(pw_list))
# 백준 단어 뒤집기2
s = input()
answer = ''
temp = ''
rever = True

for i in s:
    if i == '<':
        # 이전 temp에 저장된 글자들을 뒤집어서 추가하고 '<'까지 추가
        answer += temp[::-1] + i
        # 이후는 글자들은 <> 안에 있는 단어이기 때문에 뒤집기 안함
        rever = False
        # 새로운 글자를 담기 위해 초기화
        temp = ''
    elif i == '>':
        answer += i
        # '>' 이후 들어오는 단어는 뒤집어야 하기 때문에
        rever = True
    # rever가 False라면 <> 안에 있는 단어이기 때문에 순서대로 추가
    elif rever  == False:
        answer += i
    else:
        # 공백이 나오면 이전까지 temp에 저장된 글자들을 뒤집고 공백까지 추가
        if i == ' ':
            answer += temp[::-1] + i
            # 새로운 글자를 담기 위해 초기화
            temp = ''
        # 나머지는 뒤집기 위해 temp에 순서대로 추가
        else:
            temp += i

# 마지막 단어 처리
answer += temp[::-1]

print(answer)
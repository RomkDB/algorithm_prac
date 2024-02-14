# 백준 비밀번호 발음하기
vowel = ['a', 'e', 'i', 'o', 'u']

while True:
    pw = input()

    # 종료 조건
    if pw == 'end':
        break

    # 좋은 패스워드인지 판단하는 변수
    is_good = True
    # 모음이 포함하는지 판단하는 변수
    in_vowel = False
    # 모음 개수
    vowel_cnt = 0
    # 자음 개수
    consonatns_cnt = 0
    # 이전 글자
    prev = ''

    for i in pw:
        # 모음인 경우
        if i in vowel:
            in_vowel = True # 1번 조건(모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.)
            vowel_cnt += 1
            consonatns_cnt = 0
        # 자음인 경우
        else:
            consonatns_cnt += 1
            vowel_cnt = 0

        # 2번 조건(모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.)
        if vowel_cnt == 3 or consonatns_cnt == 3:
            is_good = False
            break

        # 3번 조건(같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.)
        if prev == i and i not in ['e', 'o']:
            is_good = False
            break

        # 다음 반복문에서 사용하기 위해 이전 글자로 업데이트
        prev = i

    if in_vowel and is_good:
        print(f'<{pw}> is acceptable.')
    else:
        print(f'<{pw}> is not acceptable.')

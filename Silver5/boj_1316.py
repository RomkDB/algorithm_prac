# 백준 그룹 단어 체커
n = int(input())
result = 0

for _ in range(n):
    s = input()
    # 확인한 글자를 저장하는 집합
    char_set = set()
    # 그룹 단어인지 반별하는 변수
    is_group = True
    # 앞 글자를 저장하는 변수
    prev_char = ''

    for i in s:
        # 1.글자(i)가 집합에 들어 있는 경우
        # 2.글자(i)가 앞에 글자와 다른 경우
        if i in char_set and i != prev_char:
            # 위 두 조건 모두 충족하면 그룹 단어가 아님
            is_group = False
            break
        # 집합에 글자(i)를 추가
        char_set.add(i)
        # 다음 반복에서 2번 조건에 사용하기 위해 이전 글자 갱신
        prev_char = i

    # 반복문 이후 그룹단어라면 카운팅
    if is_group:
        result += 1

print(result)
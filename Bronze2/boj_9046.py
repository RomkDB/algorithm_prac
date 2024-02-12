# 백준 복호화
from collections import Counter

t = int(input())

for _ in range(t):
    sentence = input().replace(" ","")
    cnt = Counter(sentence)
    # cnt : Counter({'f': 3, 'd': 2, 'e': 2, 'o': 2, 'a': 1, 's': 1, 'v': 1, 'g': 1, 'm': 1, 'n': 1})
    most_string = cnt.most_common()
    # most_string : [('f', 3), ('d', 2), ('e', 2), ('o', 2), ('a', 1), ('s', 1), ('v', 1), ('g', 1), ('m', 1), ('n', 1)]

    # 입력된 문장이 같은 알파벳으로 이루어진 경우 most_string의 원소가 1개이기 때문에
    # most_string[1] 인덱스로 접근할 수 없음(IndexError)
    try:
        if most_string[0][1] == most_string[1][1]:
            print('?')
        else:
            print(most_string[0][0])
    except:
        print(most_string[0][0])
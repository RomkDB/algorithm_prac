# 백준 파일 정리
from collections import Counter

n = int(input())
answer = []

for _ in range(n):
    file_name = input()
    # . 뒤에 확장자만 슬라이싱
    extension = file_name[file_name.find('.')+1:]
    answer.append(extension)

# (확장자, 개수) 원소들이 담긴 리스트로 변환
extension_cnt = list(Counter(answer).most_common())
# 확장자 키 기준으로 정렬
extension_cnt.sort(key=lambda x : x[0])

for i in extension_cnt:
    print(*i)
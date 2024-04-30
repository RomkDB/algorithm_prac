# 백준 18870번 좌표 압축
n = int(input())
arr_list = list(map(int, input().split()))
unique_element = list(set(arr_list))
unique_element.sort()

compression = {}

for idx, i in enumerate(unique_element):
    compression[i] = idx

for j in arr_list:
    print(compression[j], end=' ')
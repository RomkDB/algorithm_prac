# 백준 오르막길
n = int(input())
h_list = list(map(int, input().split()))
h_dif = 0
dif_list = []

for i in range(n-1):
    if h_list[i] < h_list[i+1]:
        h_dif += h_list[i+1] - h_list[i]
    else:
        dif_list.append(h_dif)
        h_dif = 0
dif_list.append(h_dif)
print(max(dif_list))
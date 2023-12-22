# 백준 유레카 이론
tri = [n*(n+1)//2 for n in range(1, 46)]
eur = [0]*1001

for i in tri:
    for j in tri:
        for k in tri:
            if i + j + k <= 1000:
                eur[i+j+k] = 1

t = int(input())
for _ in range(t):
    print(eur[int(input())])
# 백준 12100번 2048(Easy)
from copy import deepcopy

n = int(input())
board = [list(map(int, input().split())) for i in range(n)]

def change_dr(b, n):
    nb = deepcopy(b)
    
    for i in range(n):
        for j in range(n):
            nb[j][n-i-1] = b[i][j]
    
    return nb

def convert(line, n):
    new_list = [i for i in line if i]

    for i in range(1, len(new_list)):
        if new_list[i-1] == new_list[i]:
            new_list[i-1] *= 2
            new_list[i] = 0
    
    new_list = [i for i in new_list if i]
    
    return new_list + [0] * (n-len(new_list))

def dfs(n, b, cnt):
    ret = max([max(i) for i in b])

    if cnt == 0:
        return ret
    
    for _ in range(4):
        x = [convert(i, n) for i in b]
        
        if x != b:
            ret = max(ret, dfs(n, x, cnt-1))
        
        b = change_dr(b, n)
    
    return ret

print(dfs(n, board, 5))
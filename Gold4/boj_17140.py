# 백준 17140번 이차원 배열과 연산

def sort_row(row):
    counter = dict()

    for x in row:
        if x == 0:
            continue
        if x not in counter:
            counter[x] = 1
        else:
            counter[x] += 1
        
    sorted_counter = sorted(counter.items(), key=lambda x: (x[1], x[0]))
    result = []

    for val, cnt in sorted_counter:
        result += [val, cnt]
    
    return result
    
def transpose(matrix):
    row_length = len(matrix)
    column_length = len(matrix[0])
    result = [[0] * row_length for i in range(column_length)]

    for i in range(column_length):
        for j in range(row_length):
            result[i][j] = matrix[j][i]
        
    return result


def process(matrix, oper):
    if oper == 'C':
        matrix = transpose(matrix)
    max_length = 0

    for i in range(len(matrix)):
        matrix[i] = sort_row(matrix[i])
        max_length = max(max_length, len(matrix[i]))

    for i in range(len(matrix)):
        gap = max_length - len(matrix[i])
        matrix[i] += [0] * gap
        matrix[i] = matrix[i][:100]

    if oper == 'C':
        matrix = transpose(matrix)
    
    return matrix

r, c, k = map(int, input().split())
matrix = []

for i in range(3):
    matrix.append(list(map(int, input().split())))

t= 0

while True:
    row_length = len(matrix)
    column_length = len(matrix[0])

    if row_length >= r and column_length >= c:
        if matrix[r-1][c-1] == k:
            print(t)
            break
    
    if t == 100:
        print(-1)
        break

    if row_length >= column_length:
        matrix = process(matrix, 'R')
    else:
        matrix = process(matrix, 'C')
    
    t += 1
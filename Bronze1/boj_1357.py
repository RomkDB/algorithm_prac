# 백준 뒤집힌 덧셈
x, y = map(int, input().split())

def Rev(X):
    if X == 100:
        return 1
    else:
        return int(str(X)[::-1])

print(Rev(Rev(x) + Rev(y)))
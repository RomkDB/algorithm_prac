# 백준 배열 합치기
n, m = map(int, input().split())
a_arr = list(map(int,input().split()))
b_arr = list(map(int,input().split()))
c_arr = a_arr + b_arr
c_arr.sort()
print(*c_arr)
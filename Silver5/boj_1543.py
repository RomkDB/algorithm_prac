# 백준 문서 검색
s = input()
w = input()

cnt = 0
idx = 0

while idx <= len(s) - len(w):
    if s[idx:idx+len(w)] == w:
        cnt += 1
        idx += len(w)
    else:
        idx += 1

print(cnt)

# s = input()
# w = input()
# answer = s.split(w)
# print(len(answer)-1)
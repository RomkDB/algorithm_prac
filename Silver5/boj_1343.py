# 백준 폴리오미노
s = input()
poly = ''
inx = 0

while inx < len(s):
    if s[inx:inx+4] == 'XXXX':
        poly += 'AAAA'
        inx += 4
    elif s[inx:inx+2] == 'XX':
        poly += 'BB'
        inx += 2
    else:
        poly += s[inx]
        inx += 1

if 'X' in poly:
    print(-1)
else:
    print(poly)

# 다른 풀이
# s = input()
# s = s.replace('XXXX','AAAA')
# s = s.replace('XX','BB')

# if 'X' in s:
#     print(-1)
# else:
#     print(s)
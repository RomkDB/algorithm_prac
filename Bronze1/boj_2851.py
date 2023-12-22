# 백준 슈퍼 마리오
m_list = []
s = 0

for _ in range(10):
    m = int(input())
    m_list.append(m)

for i in m_list:
    if abs((s + i) - 100) <= abs(s - 100):
        s += i
    else:
        break

print(s)
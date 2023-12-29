# 백준 카드1
n = int(input())
cards = [i+1 for i in range(n)]
drop = []

while len(cards) != 1:
    drop.append(cards.pop(0))
    cards.append(cards.pop(0))

drop.append(cards[0])

print(*drop)
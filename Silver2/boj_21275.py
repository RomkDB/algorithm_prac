# 백준 폰 호석만
a, b = input().split()
answer = []

# 2~36진법에 대해서 반복
for i in range(2, 37):
    try:
        # 입력 받은 첫번째 숫자를 i 진법으로 변환
        num1 = int(a, i)
    except ValueError:
        # 변환이 안된다면 다음 진법으로 넘어감
        continue

    # 두번째 숫자도 2~36진법에 대해서 반복
    for j in range(2, 37):
        # 같은 진법이라면 다음 진법으로 넘어감
        if i == j:
            continue
        try:
            # 입력 받은 두번째 숫자를 j 진법으로 변환
            num2 = int(b, j)
        except ValueError:
            # 변환이 안된다면 다음 진법으로 넘어감
            continue
        # 변환한 2개의 숫자가 같다면 answer에 추가
        if num1 == num2:
            answer.append((num1, i, j))

if len(answer) == 0:
    print("Impossible")
elif len(answer) > 1:
    print("Multiple")
else:
    print(f"{answer[0][0]} {answer[0][1]} {answer[0][2]}")
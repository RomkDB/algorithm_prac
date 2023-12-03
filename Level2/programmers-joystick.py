# 프로그래머스 조이스틱
def solution(name):
    answer = 0
    # 좌우로 이동하는 최소 횟수는 전체길이 - 1
    move_cnt = len(name) - 1

    for i, spell in enumerate(name):
        # 상 방향키로 가는 횟수와 하 방향키로 가는 횟수 중 작은 값으로 더 해줌
        answer += min(ord(spell) - ord('A'), ord('Z') - ord(spell) + 1)
        # 다음 글자로 이동하는 인덱스
        next = i + 1

        # 이동한 위치가 전체 길이보다 작아야 하고,
        # 이동한 위치의 글자가 A라면
        # 계속 이동
        while next < len(name) and name[next] == 'A':
            next += 1
        # 좌우 방향키로 이동하는 횟수를 더함(아래 3가지 중 작은값으로)
        # 1.이전까지 계산된 최소 이동 횟수
        # 2.현재 위치에서 시작점(idx=0)으로 돌아간 다음, 남은 문자들을 처리하기 위해 다시 끝까지 이동하는 경우
        # '2*1' : 현재 위치에서 시작점으로 돌아가는데 드는 이동 횟수(왕복이기 때문에 2배)
        # 'len(name) - next' : 남은 문자들을 처리하기 위해 다시 끝까지 이동하는 횟수
        # 3.시작점에서 현재 위치까지 이동한 다음, 남은 문자들을 처리하기 위해 끝까지 갔다가 다시 돌아오는 경우
        # 'len(name) - next : 남은 문자들에 대한 이동 횟수이고, *2를 하는 이유는 다시 돌아와야 하기 때문에
        move_cnt = min([move_cnt, 2 * i + len(name) - next, i + 2 * (len(name) - next)])

    # 총 조작 횟수에서 좌우 이동하는 횟수를 더함
    answer += move_cnt

    return answer

print(solution('JEROEN'))
print(solution('JAN'))
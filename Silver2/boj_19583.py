# 백준 싸이버개강총회
# 개인적으로 종료조건이 명확하지 않은 것 같음

# 처음에는 스트리밍을 끝낸 시간(Q)보다
# 채팅기록 시간이 이후인 입력값은 필요없는 데이터이니깐
# 입력을 받지 않으면 되는거 아닌가 생각했지만
# 문제의 입력값은 다 받아야 한다는 오류 케이스가 있음

# 다른 분들처럼 EOF가 나올때까지 반복하도록
# try/execpt 문으로 작성함

# 백준 사이트에서 제출 시 시간초과 발생
# sys.stdin.readline() 사용

s, e, q = input().split()
attend_list = {}
cnt = 0

s_time = int(s.replace(':',''))
e_time = int(e.replace(':',''))
q_time = int(q.replace(':',''))

while True:
    try:
        time, name = input().split()
        c_time = int(time.replace(':',''))

        if c_time <= s_time:
            attend_list[name] = 1
        elif e_time <= c_time <= q_time:
            # 여러번 채팅을 작성하는 경우인 중복을 고려하였는데
            # 생각해보니 첫번째 if문과 elif 조건에서 필터링 됨
            # if name in attend_list and attend_list[name] == 1:
            if name in attend_list:
                cnt += 1
                # attend_list[name] += 1
                del attend_list[name]
    except:
        break

print(cnt)

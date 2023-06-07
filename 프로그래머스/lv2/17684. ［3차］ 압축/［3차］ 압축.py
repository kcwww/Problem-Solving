from collections import deque

def solution(msg):
    answer = []
    aldic = {}
    # 길이가 1인 모든 단어포함 하도록 초기화
    # 돌아오기 ) 사전에서 현재 입력과 일치 -> 가장 긴 문자열 w
    # w 에 해당하는 사전의 색인 번호 출력 -> w 제거
    # 다음 글자가 있다면 w+c 단어 사전에 등록
    # 돌아가기
    deq = deque()
    al = ord('A')
    for i in range(1,27):
        aldic[chr(al)] = i
        al += 1
    al = 27
    # 메세지 스택에 담으면서 검사 -> 출력, 사전에 추가, 현재입력 제거
    for m in msg:
        deq.append(m)
        w = ''.join(deq)
        if w in aldic:
            continue
        else:
            aldic[w] = al
            al += 1
            c = deq.pop()
            w = ''.join(deq)
            answer.append(aldic[w])
            deq = deque([c])
    w = ''.join(deq)
    answer.append(aldic[w])
    return answer
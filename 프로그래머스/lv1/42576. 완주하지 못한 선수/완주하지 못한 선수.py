def solution(participant, completion):
    com = {}
    answer = ''
    for name in participant:
        com[name] = 0
    for name in participant:
        com[name] -= 1
    for name in completion:
        com[name] += 1
    for no in com:
        if com[no] != 0:
            answer += no
    
    return answer
def solution(answers):
    three_man = {1 : [1,2,3,4,5], 2 : [2,1,2,3,2,4,2,5], 3 : [3,3,1,1,2,2,4,4,5,5]}
    count = {'one' : 0, 'two' : 0, 'three' : 0}
    problem = len(answers)
    
    idx = 0
    for i in range(problem):
        if (answers[i] == three_man[1][idx]):
            count['one'] += 1
        idx += 1
        if (idx == 5):
            idx = 0
    
    idx = 0
    for i in range(problem):
        if (answers[i] == three_man[2][idx]):
            count['two'] += 1
        idx += 1
        if (idx == 8):
            idx = 0
    
    idx = 0
    for i in range(problem):
        if (answers[i] == three_man[3][idx]):
            count['three'] += 1
        idx += 1
        if (idx == 10):
            idx = 0
    
    num = max(count[x] for x in count)
    answer = []
    if (num == count['one']):
        answer.append(1)
    if (num == count['two']):
        answer.append(2)
    if (num == count['three']):
        answer.append(3)
    
    return answer
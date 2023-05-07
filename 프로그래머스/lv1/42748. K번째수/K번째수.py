def solution(array, commands):
    answer = []
    
    for i in commands:
        temp = array
        temp = temp[i[0] - 1: i[1]]
        temp.sort()
        answer.append(temp[i[2] - 1])
        
    return answer
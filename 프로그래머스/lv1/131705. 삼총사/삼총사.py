def solution(number):
    student = len(number)

    answer = 0
    for first in range(student):
        for second in range(first + 1, student):
            for third in range(second + 1, student):
                value = number[first] + number[second] + number[third]
                if (value == 0):
                    answer += 1
    return answer
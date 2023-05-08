def solution(numbers, hand):
    answer = ''
    phone = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    left = [3,0]
    right = [3,2]
    
    for num in numbers:
        if (num == 1 or num == 4 or num == 7):
            answer += 'L'
            for p in phone:
                if num in p:
                    left[0] = phone.index(p)
                    left[1] = 0
        elif (num == 3 or num == 6 or num == 9):
            answer += 'R'
            for p in phone:
                if num in p:
                    right[0] = phone.index(p)
                    right[1] = 2
        else:
            for p in phone:
                if num in p:
                    x = phone.index(p)
                    arrive_l = abs(x - left[0]) + abs(1 - left[1])
                    arrive_r = abs(x - right[0]) + abs(1 - right[1])
                    if (arrive_l == arrive_r):
                        if (hand == "right"):
                            right[0] = x
                            right[1] = 1
                            answer += 'R'
                        else:
                            answer += 'L'
                            left[0] = x
                            left[1] = 1
                    elif (arrive_l > arrive_r):
                        right[0] = x
                        right[1] = 1
                        answer += 'R'
                    else:
                        answer += 'L'
                        left[0] = x
                        left[1] = 1

    return answer
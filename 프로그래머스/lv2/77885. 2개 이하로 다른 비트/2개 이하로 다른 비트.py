def solution(numbers):
    answer = []
    for num in numbers:
        if (num % 2) == 0:
            answer.append(num + 1)
        else:
            num = list('0' + str(bin(num))[2:])
            idx = len(num) - 1
            for n in range(idx, -1, -1):
                if (num[n] == '0'):
                    num[n] = '1'
                    num[n+1] = '0'
                    num = ''.join(num)
                    break
                idx += 1
            num = int(num, 2)
            answer.append(num)
    return answer
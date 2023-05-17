def solution(fees, records):
    answer = []
    car = {}
    
    
    for r in records:
        time, num, io = r.split()
        h, m = map(int, time.split(':'))
        time = h * 60 + m
        if num not in car:
            car[num] = [0, 0, 0]
        
        if io == 'IN':
            car[num][2] = 'IN'
            car[num][1] = time
        elif io == 'OUT':
            car[num][2] = 'OUT'
            car[num][0] += time - car[num][1]
            car[num][1] = 0
    
    for i in car:
        if (car[i][2] == 'IN'):
            car[i][2] == 'OUT'
            time = 23 * 60 + 59
            car[i][0] += time - car[i][1]
            car[i][1] = 0
    
    car = dict(sorted(car.items()))

    for c in car:
        fee = car[c][0] - fees[0]
        if (fee <= 0):
            answer.append(fees[1])
        else:
            if fee % fees[2] != 0:
                fee = fee // fees[2] + 1
            else:
                fee = fee // fees[2]
            fee = fees[1] + fee * fees[3]
            answer.append(fee)
    return answer
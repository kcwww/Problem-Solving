def compare_today(compare_day, today):
    t_year, t_month, t_day = map(int, today.split('.'))
    if (t_year > compare_day[0]):
        return (-1)
    elif (compare_day[0] > t_year):
        return (1)
    if (t_month > compare_day[1]):
        return (-1)
    elif (compare_day[1] > t_month):
        return (1)
    if (t_day > compare_day[2]):
        return (-1)
    elif (compare_day[2] > t_day):
        return (1)
    return (1)

def solution(today, terms, privacies):
    term_dic = {}
    answer = []
    idx = 1
    for term in terms:
        key , value = term.split()
        term_dic[key] = int(value)

    for parse in privacies:
        contract, term = parse.split()
        c_year, c_month, c_day = map(int, contract.split('.'))
        c_day += term_dic[term] * 28
        while (c_day // 28):
            c_day -= 28
            c_month += 1
        if (c_day == 0):
            c_day = 28
            c_month -= 1
        elif (c_day == 1):
            c_day = 29
            c_month -= 1
        c_day -= 1
        
        if (c_month == 0):
            c_month = 12
            c_year -= 1
        while (c_month // 12):
            c_month -= 12
            c_year += 1
        if (c_month == 0):
            c_month = 12
            c_year -= 1
        result = compare_today([c_year, c_month, c_day], today)
        if (result == -1):
            answer.append(idx)
        idx += 1
    return answer
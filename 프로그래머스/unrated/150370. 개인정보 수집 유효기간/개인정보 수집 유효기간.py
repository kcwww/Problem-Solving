def get_today(today):
    year, month, day = map(int, today.split('.'))
    return (year * 12 * 28 + month * 28 + day)

def solution(today, terms, privacies):
    terms_dic = {}
    answer = []
    idx = 1
    
    for term in terms:
        key , value = term.split()
        terms_dic[key] = int(value)
    
    today = get_today(today)
    for parse in privacies:
        contract, term = parse.split()
        c_year, c_month, c_day = map(int, contract.split('.'))
        c_day += terms_dic[term] * 28
        compare_day = c_year * 12 * 28 + c_month * 28 + c_day
        if (compare_day <= today):
            answer.append(idx)
        idx += 1
    return answer

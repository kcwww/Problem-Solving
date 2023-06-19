def solution(today, terms, privacies):
    today = list(map(int, today.split('.')))
    today = today[0] * 12 * 28 + today[1] * 28 + today[2]
    answer = []
    term = {}
    for te in terms:
        t, n = te.split()
        term[t] = int(n)
    
    idx = 1
    for privacie in privacies:
        date, t = privacie.split()
        date = list(map(int, date.split('.')))
        date = date[0] * 12 * 28 + date[1] * 28 + date[2] + term[t] * 28
        if today >= date:
            answer.append(idx)
        idx += 1
    return answer
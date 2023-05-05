def solution(survey, choices):
    KBTI = {"R" : 0, "T" : 0, "C" : 0, "F" : 0, "J" : 0, "M" : 0, "A" : 0, "N" : 0}
    idx = len(choices)
    for i in range(idx):
        choices[i] -= 4
        if (choices[i] < 0):
            choices[i] = -choices[i]
            survey[i] = survey[i][::-1]
    
    for i in range(idx):
        KBTI[survey[i][0]] += choices[i]
    answer = ''
    if (KBTI['R'] > KBTI['T']):
        answer += 'T'
    else:
        answer += 'R'
    if (KBTI['C'] > KBTI['F']):
        answer += 'F'
    else:
        answer += 'C'
    if (KBTI['J'] > KBTI['M']):
        answer += 'M'
    else:
        answer += 'J'
    if (KBTI['A'] > KBTI['N']):
        answer += 'N'
    else:
        answer += 'A'
    return answer
def solution(name, yearning, photo):
    memory = {}
    answer = []

    for n in name:
        memory[n] = 0
    i = 0
    for key in memory:
        memory[key] = yearning[i]
        i += 1
            
    for p in photo:
        m_num = 0
        for n in p:
            if n in memory:
                m_num += memory[n]
        answer.append(m_num)
    return answer
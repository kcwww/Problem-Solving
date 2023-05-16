def solution(cards):
    group = []
    for i in range(len(cards)):
        m_group = []
        idx = i
        while cards[idx] != 0:
            m_group.append(cards[idx])
            nm = cards[idx]
            cards[idx] = 0
            idx = nm - 1
        if (m_group == []):
            continue
        group.append(m_group)
    answer = list(len(x) for x in group)
    answer.sort()
    return answer[-1] * answer[-2] if len(answer) > 1 else 0
def solution(id_list, report, k):
    answer = []
    reports = {}
    for i in id_list:
        reports[i] = []
    result = {}
    for r in report:
        a, b = r.split()
        if a in reports:
            if b in reports[a]:
                continue
            reports[a].append(b)
            if b in result:
                result[b] += 1
            else:
                result[b] = 1
        else:
            reports[a] = [b]
            if b in result:
                result[b] += 1
            else:
                result[b] = 1

    for ke, v in result.items():
        if v >= k:
            answer.append(ke)
    a = []
    for i in id_list:
        cnt = 0
        for r in reports[i]:
            if r in answer:
                cnt += 1
        a.append(cnt)
    return a
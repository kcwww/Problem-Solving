def solution(skill, skill_trees):
    #tree를 순회하면서 검사
    answer = 0
    skill = list(skill)
    
    for s in skill_trees:
        re = []
        flag = 0
        for c in s:
            if c in skill:
                re.append(c)
        for i, r in enumerate(re):
            if (r != skill[i]):
                flag = 1
        if (flag == 0):
            answer += 1
    return answer
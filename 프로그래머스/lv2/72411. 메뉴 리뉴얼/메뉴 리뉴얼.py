from itertools import combinations

def solution(orders, course):
    #코스별 조합
    #오더 순회하면서 갯수 새고 가장 큰수 넣기
    answer = []
    for num in course:
        menu_dict = {}
        for o in orders:
            menu = combinations(o, num)
            for x in menu:
                x = sorted(x)
                x = ''.join(x)
                if (x in menu_dict):
                    menu_dict[x] += 1
                else:
                    menu_dict[x] = 1
        x = list(menu_dict.values())
        if (x):
            x = max(x)
        else:
            x = 0
        if (x <= 1):
            continue
        for m in menu_dict:
            if (menu_dict[m] == x):
                answer.append(''.join(m))
        
        
    return sorted(answer)
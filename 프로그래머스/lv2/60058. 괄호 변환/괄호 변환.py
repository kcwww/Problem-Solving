def check_paren(paren):
    stack = []
    if paren[0] == ')':
        return False
    for p in paren:
        if p == ')' and len(stack) > 0:
            c = stack.pop()
            if (c != '('):
                return False
        elif p == ')':
            return False
        else:
            stack.append(p) 
    return True

def one_two_three(p):
    if p == "":
        return ""
    l, r = 0, 0
    u, v = '', ''
    for i in p:
        if (l != 0 and l == r):
            v += i
            continue
        if (i == '('):
            l += 1
        elif (i == ')'):
            r += 1
        u += i
    if check_paren(u):
        u += one_two_three(v)
    else:
        new_str = '('
        new_str += one_two_three(v)
        new_str += ')'
        u = list(u)
        u = map(lambda x : ')' if x == '(' else '(', u[1:len(u) - 1])
        u = new_str + ''.join(u)
    return u

def solution(p):
    if check_paren(p):
        return p
    return one_two_three(p)
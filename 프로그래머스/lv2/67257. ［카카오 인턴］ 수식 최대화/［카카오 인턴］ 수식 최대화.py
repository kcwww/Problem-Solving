from itertools import combinations, permutations

def tokenizer(expression):
    num = []
    oper = []
    n = ''
    for i in expression:
        if (i == '-' or i == '*' or i == '+'):
            num.append(int(n))
            num.append(i)
            oper.append(i)
            n = ''
        else:
            n += i
    num.append(int(n))
    return [num, oper]
            
        
def calculate(num1, num2, oper):
    if (oper == '-'):
        return num1 - num2
    if (oper == '*'):
        return num1 * num2
    if (oper == '+'):
        return num1 + num2
    
def solution(expression):
    #연산자 와 숫자를 나누어 담음
    #순서 완전 탐색
    answer = 0
    expression = tokenizer(expression)
    oper = list(set(expression[1]))
    oper = permutations(oper, len(oper))
    expression = expression[0]
    print(expression)
    for p in oper:
        temp = [x for x in expression]
        for o in p:
            flag = 0
            stack = []
            for ex in temp:
                stack.append(ex)
                if (flag == 1):
                    flag = 0
                    num2 = stack.pop()
                    c = stack.pop()
                    num1 = stack.pop()
                    stack.append(calculate(num1, num2, c))
                elif (ex == o):
                    flag = 1
            temp = stack
        if (answer < abs(temp[0])):
            answer = abs(temp[0])
            
    return answer
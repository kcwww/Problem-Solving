def solution(brown, yellow):
    # brown = 2x + 2(y-2)
    # yellow = (x - 2) * (y - 2) 
    # y = num - x
    # yellow = (x - 2) * (num - 2 - x) 
    # yellow = -x2 + (num - 2)x + 2x - 2*(num - 2)
    # x2 -numx + 2*(num - 2) + yellow = 0
    # ax^2 + bx + c
    num = ((brown // 2) + 2)
    b = -num
    c = 2*(num - 2) + yellow
    return [int((-b + (b**2 -4*c)**(1/2)) // 2), int((-b - (b**2 -4*c)**(1/2)) // 2)]
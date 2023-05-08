def check_basket(basket):
    l = len(basket)
    num = basket[-1]
    if (l > 1 and num == basket[-2]):
        basket.pop()
        basket.pop()
        return 2
    return 0

def solution(board, moves):
    answer = 0
    basket = []
    for m in moves:
        for b in board:
            if (b[m - 1] != 0):
                basket.append(b[m - 1])
                b[m - 1] = 0
                answer += check_basket(basket)
                break
            
    
    return answer
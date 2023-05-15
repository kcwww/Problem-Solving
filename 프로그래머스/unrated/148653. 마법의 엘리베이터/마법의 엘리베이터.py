def solution(storey):
    answer = 0
    while storey:
        
        if (storey % 10) > 5:
            num = (10 - (storey % 10))
            storey += num
            answer += num
        
        elif (storey % 10) == 5:
            next_st = (storey // 10) % 10
            if (next_st >= 5):
                num = (10 - (storey % 10))
                storey += num
                answer += num
                
            else:
                num = (storey % 10)
                storey -= num
                answer += num
            
            
        else:
            num = (storey % 10)
            storey -= num
            answer += num
        storey //= 10
    return answer
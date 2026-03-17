def solution(diffs, times, limit):
    answer = 0
    left = 1
    right = 100000
    length = len(diffs)
    
    while (left <= right):
        level = (left + right) // 2
        
        
        # diff <= level -> time_cur
        # diff > level -> (diff - level) * (time_cur + time_prev) + time_cur
        
        solved = 0
        for i in range(length):
            diff = diffs[i]
            time = times[i]
            time_prev = times[i - 1] if i > 0 else 0
            
            if (diff <= level):
                solved += time
            elif (diff > level):
                solved += (diff - level) * (time + time_prev) + time
                
            if (solved > limit):
                break
        if (solved > limit):
            left = level + 1
        elif (solved <= limit):
            answer = level
            right = level - 1
            
    
    return answer
def solution(book_time):
    answer = 0
    book_time.sort(key=lambda x : x[0])
    
    rooms = []
    for i in range(len(book_time)):
        sh , sm = map(int,book_time[i][0].split(':'))
        sh *= 60
        lh , lm = map(int,book_time[i][1].split(':'))
        lh *= 60
        book_time[i] = [sh + sm, lh + lm]
    
    for room in book_time:
        if (len(rooms) == 0):
            answer += 1
            rooms.append(room)
        else:
            flag = 0
            for i,r in enumerate(rooms):
                if (room[0] >= r[1] + 10):
                    rooms[i] = room
                    flag = 1
                    break
            if (flag == 0):
                answer += 1
                rooms.append(room)
    
    
                    
        
    return answer
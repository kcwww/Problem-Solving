def solution(a, b):
    date = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    day = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    days = 0
    for i in range(1, a):
        days += date[i]
    days += b
    return day[days % 7]
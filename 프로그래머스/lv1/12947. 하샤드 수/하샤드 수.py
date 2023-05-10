def solution(x):
    an = 0
    for i in str(x):
        an += int(i)
    
    return (x % sum(int(i) for i in str(x))) == 0
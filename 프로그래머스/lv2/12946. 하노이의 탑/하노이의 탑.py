def hanoi(start, via, destination, n):
    if n == 1:
        return [[start, destination]]
    return hanoi(start, destination, via, n - 1) + [[start, destination]]+ hanoi(via, start, destination, n - 1)

def solution(n):
    #2 hanoi(2)
    #3 hanoi(2) -> via 로 옮기고 맨 밑 원판 옮기고 via->end 로 hanoi(2) 다시
    #4 hanoi(3) -> via 로 옮기고 맨 밑 원판 옮기고 via->end 로 hanoi(3) 다시
    return hanoi(1, 2, 3, n)
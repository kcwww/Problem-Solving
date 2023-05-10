def solution(arr):
    arr.pop(arr.index(min(arr)))
    return arr if len(arr) >= 1 else [-1]
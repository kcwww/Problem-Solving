from itertools import permutations
def solution(numbers):
    a = list(map(str, numbers))
    a.sort(key=lambda x :  x * 4)
    return ''.join(a[::-1]) if a[-1] != '0' else '0'
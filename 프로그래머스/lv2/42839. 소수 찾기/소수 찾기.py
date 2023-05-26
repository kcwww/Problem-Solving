from itertools import permutations

def check_prime(num):
    if num == 1:
        return 0
    if num != 2 and num % 2 == 0:
        return 0
    half = int(num ** (1/2))
    for i in range(2, half + 1):
        if num % i == 0:
            return 0
    return 1
        

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    print(numbers)
    size = len(numbers)
    nums = {}

    for n in numbers:
        if n == '2' or n == '3' or n == '5' or n == '7':
            nums[int(n)] = 1

        
    for i in range(2, size + 1):
        a = list(permutations(numbers, i))
        for n in a:
            num = int(''.join(n))
            nums[num] = 1
    for n in nums:
        answer += check_prime(n)
        
    return answer
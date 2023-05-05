def solution(food):
    answer = '0'
    
    foods = len(food) - 1
    for i in range(foods, 0, -1):
        add_food = food[i] // 2
        answer = str(i) * add_food + answer + str(i) * add_food
    return answer
def solution(files):
    answer = []
    # head 정렬
    # numbers 정렬
    # tail 둘다 같으면 입력순서
    # [헤드 넘버 테일 인덱스]
    idx = 0
    for file in files:
        head = ''
        number = ''
        tail = ''
        i = 0
        while not file[i].isdigit():
            head += file[i]
            i += 1
        head = head.lower()
        while i < len(file) and file[i].isdigit():
            number += file[i]
            i += 1
        while i < len(file):
            tail += file[i]
            i += 1
        answer.append([head, int(number), tail, idx])
        idx += 1 

    answer.sort(key=lambda x : (x[0], x[1], x[3]))

    return list(files[i[3]] for i in answer)
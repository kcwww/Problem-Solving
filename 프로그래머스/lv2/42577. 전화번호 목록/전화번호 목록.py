def solution(phone_book):
    stack = []
    answer = True
    book = {}
    phone_book.sort(key=len)
    for p in phone_book:
        phone_num = ''
        for c in p:
            phone_num += c
            if phone_num in book:
                return False
        book[phone_num] = 1
    return answer
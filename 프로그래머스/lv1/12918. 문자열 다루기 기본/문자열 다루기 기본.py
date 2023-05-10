def solution(s):
    for c in s:
        if not (ord(c) >= ord('0') and ord(c) <= ord('9') and (len(s) == 4 or len(s) == 6)):
            return False
    return True
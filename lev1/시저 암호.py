def solution(s, n):
    answer = ''
    
    for c in s:
        if c.isalpha():
            if c.islower():
                answer += chr((ord(c) - ord('a') + n) % 26 + ord('a'))
            elif c.isupper():
                answer += chr((ord(c) - ord('A') + n) % 26 + ord('A'))
        else:
            answer += c
    return answer
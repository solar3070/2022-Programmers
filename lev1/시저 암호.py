def solution(s, n):
    answer = ''
    
    for c in s:
        if c.isalpha():
            if c.islower() and ord(c) + n > ord('z'):
                answer += chr(ord(c) - 26 + n)
            elif c.isupper() and ord(c) + n > ord('Z'):
                answer += chr(ord(c) - 26 + n)
            else:
                answer += chr(ord(c) + n)
        else:
            answer += c
    return answer
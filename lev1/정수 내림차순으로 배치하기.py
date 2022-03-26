def solution(n):
    answer = 0
    
    lst = []
    while n != 0:
        lst.append(n % 10)
        n //= 10
    lst.sort(reverse = True)
    
    for n in lst:
        answer = answer * 10 + n 
        
    return answer
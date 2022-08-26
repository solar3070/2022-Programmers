def solution(price, money, count):
    answer = 0
    
    tmp = 0
    for i in range(1, count + 1):
        tmp += price * i
        
    answer = tmp - money if tmp > money else 0
    
    return answer
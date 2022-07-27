def solution(arr, divisor):
    answer = []
    
    for n in arr:
        if n % divisor == 0:
            answer.append(n) 
    answer.sort()   
    if len(answer) < 1: answer.append(-1)
    
    return answer
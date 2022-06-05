def solution(n):
    answer = 0
    
    for i in range(2, n + 1):
        prime  = 1
        for j in range(2, i):
            if i % j == 0:
                prime = 0
                break
        if prime == 1:
            answer += 1
    
    return answer
def solution(left, right):
    answer = 0
    
    for n in range(left, right + 1):
        total = 2
        for i in range(2, n):
            if n % i == 0:
                total += 1
        if total % 2 == 0 and n != 1:
            answer += n
        else:
            answer -= n
    
    return answer
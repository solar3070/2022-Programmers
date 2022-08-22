def solution(numbers):
    answer = 0
    
    numbers.sort()
    for n in range(10):
        if n not in numbers:
            answer += n
    
    return answer
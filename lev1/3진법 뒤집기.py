def solution(n):
    answer = 0
    
    lst = []
    while n > 0:
        lst.append(n % 3)
        n //= 3

    for i in range(len(lst)):
        answer += 3 ** i * lst[len(lst) - (i + 1)]
    
    return answer
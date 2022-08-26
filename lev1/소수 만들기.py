from itertools import combinations

def solution(nums):
    answer = 0
    
    for lst in combinations(nums, 3):
        prime = 1
        for i in range(2, int(sum(lst) ** 0.5) + 1):
            if sum(lst) % i == 0:
                prime = 0
                break
        if prime == 1:
            answer += 1

    return answer
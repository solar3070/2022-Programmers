def solution(nums):
    maxN = len(set(nums))   
    return len(nums) // 2 if maxN > len(nums) // 2 else maxN
def solution(lottos, win_nums):
    rank = [1, 2, 3, 4, 5, 6, 6]
    
    count = 0
    for lotto in lottos:
        if lotto in win_nums:
            count += 1
    
    return [rank[6-lottos.count(0)-count], rank[6-count]]
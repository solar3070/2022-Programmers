def solution(N, stages):
    answer = {}
    
    cnt = len(stages)
    for i in range(1, N + 1):
        userN = stages.count(i)
        answer[i] = userN / cnt if userN else 0
        cnt -= userN
        
    return sorted(answer, key=lambda x : answer[x], reverse=True)
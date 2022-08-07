def solution(n, lost, reserve):
    answer = 0
    
    r_tmp = list(set(reserve) - set(lost))
    l_tmp = list(set(lost) - set(reserve))
    answer = len(reserve) - len(r_tmp)
    
    l_tmp.sort()
    r_tmp.sort()
    
    for l in l_tmp:
        if l - 1 in r_tmp:
            answer += 1
            r_tmp.remove(l - 1)
        elif l + 1 in r_tmp:
            answer += 1
            r_tmp.remove(l + 1)
            
    return n - len(lost) + answer
def solution(s):
    answer = ''
    
    mid = len(s) // 2      
    answer = s[mid] if len(s) % 2 else s[mid-1:mid+1] 
    
    return answer
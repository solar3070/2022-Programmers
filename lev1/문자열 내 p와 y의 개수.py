def solution(s):
    p_count = y_count = 0
    
    for ch in s.lower():
        if ch == 'p':
            p_count += 1
        elif ch == 'y':
            y_count += 1

    return p_count == y_count
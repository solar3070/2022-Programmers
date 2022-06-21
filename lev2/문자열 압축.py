def solution(s):
    min = len(s)
    for i in range(1, len(s) // 2 + 1):
        answer = ""
        count = 1
        before = s[0 : i]
        for j in range(i, len(s) + 1, i):
            current = s[j : j + i]
            if before == current:
                count += 1
            else:
                if count != 1:
                    answer += str(count)
                answer += before
                if len(current) < len(before):
                    answer += current  
                before = current
                count = 1
        if len(answer) < min:
            min = len(answer)  
    return min
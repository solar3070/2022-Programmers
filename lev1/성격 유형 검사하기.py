def solution(survey, choices):
    answer = ''
    score = {x: 0 for x in set(list(''.join(survey)))}
    
    for i in range(len(survey)):
        if choices[i] >= 5:
            score[survey[i][1]] += choices[i] % 4
        else:
            score[survey[i][0]] += 4 - choices[i]
    
    lst = ["RT", "CF", "JM", "AN"]
    for l in lst:     
        if l[0] not in score:
            answer += l[0]
        else:    
            answer += l[0] if score[l[0]] >= score[l[1]] else l[1]
    
    return answer
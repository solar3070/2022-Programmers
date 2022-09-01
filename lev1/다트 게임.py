def solution(dartResult):
    area = {'S': 1, 'D': 2, 'T': 3}
    
    idx = []
    for i in range(len(dartResult)):
        if dartResult[i].isdigit() == False and dartResult[i + 1].isdigit():
            idx.append(i + 1)
        if len(idx) == 2:
            break      
    lst = []
    lst.append(dartResult[:idx[0]])
    lst.append(dartResult[idx[0]:idx[1]])
    lst.append(dartResult[idx[1]:])

    score = [0] * 3
    bonus = [0] * 3
    for i in range(3):
        for j in range(len(lst[i])):
            if lst[i][j].isdigit() == False:
                score[i] = int(lst[i][:j])
                bonus[i] = lst[i][j:]
                break
    
    for i in range(len(score)):
        score[i] = score[i] ** area[bonus[i][0]]
        if len(bonus[i]) >= 2:
            if bonus[i][1] == '*':
                score[i] *= 2
                if i != 0:
                    score[i - 1] *= 2
            elif bonus[i][1] == '#':
                score[i] *= -1          
                
    return sum(score)
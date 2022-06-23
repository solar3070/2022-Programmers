from itertools import combinations

def solution(orders, course):
    answer = []
    
    for n in course:   
        combList = []
        for menu in orders:
            menu = sorted(menu)
            combList += set(combinations(menu, n))
            
        combList = set(combList)
        
    
    
        max = 0
        temp = []
        for comb in combList:
            count = 0
            for menu in orders:
                flag = True
                for c in comb:
                    if c not in list(menu):
                        flag = False
                        break
                if flag == True:
                    count += 1
            if count > max:
                max = count;
                temp = ["".join(comb)]
            elif count == max:
                temp.append("".join(comb))
        if max > 1:
            answer += temp
    answer.sort()
    
    return answer
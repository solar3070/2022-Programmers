def checkCorrectStr(str): 
    l_cnt = r_cnt = 0
    
    for ch in str:
        if ch == "(":
            l_cnt += 1
        else:
            r_cnt += 1
        
        if r_cnt > l_cnt:
            return 0
        
    return 1    

def reverseStr(str):
    reverse = ""
    
    for ch in str:
        if ch == "(":
            reverse += ")"
        else:
            reverse += "("
            
    return reverse
            
def separateStr(str):
    if str == "":
        return ""
    
    u = v = ""
    l_cnt = r_cnt = 0
    for i in range(len(str)):
        if  str[i] == "(":
            l_cnt += 1
        else:
            r_cnt += 1
        
        if l_cnt == r_cnt:
            u = str[:i + 1]
            v = "" if i + 1 >= len(str) else str[i + 1:]
            break
    
    temp = ""
    if checkCorrectStr(u):
        temp = u + separateStr(v)
    else:
        temp = "(" + separateStr(v) + ")" + reverseStr(u[1:-1])
        
    return temp

def solution(p):
    return separateStr(p)
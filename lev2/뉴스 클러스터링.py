import math

def createMultiSet(s):
    tmp_set = []
    m_set = []
    
    for i in range(len(s)):
        tmp_set.append(s[i:i+2])
        
    for elem in tmp_set:
        if len(elem) == 2 and elem.isalpha():
            m_set.append(elem.upper())
    
    return m_set

def getIntersection(m_set1, m_set2):
    tmp_set = m_set2[:]
    
    cnt = 0 
    for elem in m_set1:
        if elem in tmp_set:
            cnt += 1
            tmp_set.remove(elem)
    return cnt

def solution(str1, str2):
    answer = 0
    
    m_set1 = createMultiSet(str1)
    m_set2 = createMultiSet(str2)
    
    i_num = getIntersection(m_set1, m_set2)
    u_num = len(m_set1) + len(m_set2) - i_num
    
    print(m_set1, m_set2)
    print(i_num, u_num)

    if i_num == 0 and u_num == 0:
        answer = 65536
    else:
        answer = math.trunc(i_num / u_num * 65536)
    
    return answer
import re
    
def solution(new_id):
    symbols = ['-', '_', '.']
    
    #1
    new_id = new_id.lower()
    #2
    temp = []
    for i in range(len(new_id)):
        if new_id[i].isalpha() or new_id[i].isdigit() or new_id[i] in symbols:
            temp.append(new_id[i])
    temp = ''.join(temp)
    #3
    temp = re.sub('\.\.*', '.', temp)
    #4
    temp = re.sub('\A\.', '', temp)
    if len(temp) >= 1 and temp[-1] == '.':
        temp = temp[:-1]
    #5
    if temp == '':
        temp = 'a'
    #6
    if len(temp) >= 16:
        temp = temp[:15]
        if len(temp) >= 1 and temp[-1] == '.':
            temp = temp[:-1]
    #7
    while len(temp) <= 2:
        temp += temp[-1]
    
    return temp
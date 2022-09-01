def solution(id_list, report, k):
    answer = [0] * len(id_list)
    dict_id = {id: 0 for id in id_list}
    
    for r in set(report):
        dict_id[r.split()[1]] += 1
        
    for r in set(report):
        if dict_id[r.split()[1]] >= k:
            answer[id_list.index(r.split()[0])] += 1
    
    return answer
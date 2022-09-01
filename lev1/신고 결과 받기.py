def solution(id_list, report, k):
    dict_id = {id: 0 for id in id_list}
    temp = list(set(report))
    for r in temp:
        dict_id[r.split()[1]] += 1
    
    report_user = []
    for key, value in dict_id.items():
        if value >= k:
            report_user.append(key)

    dict_id = {id: 0 for id in id_list}
    for r in temp:
        if r.split()[1] in report_user:
            dict_id[r.split()[0]] += 1
    
    return list(dict_id.values())
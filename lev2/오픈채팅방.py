def solution(record):
    answer = []
    
    data = {}
    for str in record:
        arr = str.split(" ")
        if arr[0] == "Enter" or arr[0] == "Change":
            data[arr[1]] = arr[2]

    for str in record:
        arr = str.split(" ")
        if arr[0] == "Enter":
            answer.append(data[arr[1]] + "님이 들어왔습니다.")
        elif arr[0] == "Leave":
            answer.append(data[arr[1]] + "님이 나갔습니다.")
    
    return answer
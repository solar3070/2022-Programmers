def binary(len, n):
    answer = [0] * len
    for i in range(len - 1, -1, -1):
        if n == 0:
            break
        answer[i] = n % 2
        n //= 2
    return answer

def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        tmp = ""
        map1 = binary(n, arr1[i])
        map2 = binary(n, arr2[i])
        for j in range(n):
            tmp += " " if map1[j] == 0 and map2[j] == 0 else "#"  
        answer.append(tmp)
    return answer
def solution(numbers, hand):
    answer = ''
    
    lPos = [3, 0]
    rPos = [3, 2]
    for n in numbers:
        print(n)
        if n in [1, 4, 7]:
            lPos = [(n - 1) // 3, (n - 1) % 3]
            answer += 'L'
        elif n in [3, 6, 9]:
            rPos = [(n - 1) // 3, (n - 1) % 3]
            answer += 'R'
        else:                
            nPos = [3, 1] if n == 0 else [(n - 1) // 3, (n - 1) % 3]
            lDis = abs(nPos[0] - lPos[0]) + abs(nPos[1] - lPos[1])
            rDis = abs(nPos[0] - rPos[0]) + abs(nPos[1] - rPos[1])
            print(nPos, lPos, rPos)
            print(lDis, rDis)
            
            if lDis == rDis:
                if hand == 'left':
                    lPos = nPos
                    answer += 'L'
                else:
                    rPos = nPos
                    answer += 'R'
            elif lDis < rDis:
                lPos = nPos
                answer += 'L'
            else:
                rPos = nPos
                answer += 'R'

    return answer
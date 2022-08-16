def solution(board, moves):
    answer = 0
    
    basket = []
    for m in moves:
        for b in board:
            if b[m-1] != 0:  
                if len(basket) >= 1:
                    if basket[-1] == b[m-1]:
                        answer += 2
                        basket.pop() 
                        b[m-1] = 0
                        break
                        
                basket.append(b[m-1])
                b[m-1] = 0
                break

    return answer
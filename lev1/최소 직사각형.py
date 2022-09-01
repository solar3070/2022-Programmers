def solution(sizes):
    for size in sizes:
        size.sort(reverse=True)
        
    m1 = m2 = 0
    for size in sizes:
        if size[0] > m1:
            m1 = size[0]
        if size[1] > m2:
            m2 = size[1]

    return m1 * m2
def solution(x):
    x_sum = 0
    tmp = x
    while tmp > 0:
        x_sum += tmp % 10
        tmp //= 10
    return False if x % x_sum != 0 else True
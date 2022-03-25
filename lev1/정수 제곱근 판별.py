import math

def solution(n):
    s = math.sqrt(n)
    return (int(s) + 1) ** 2 if s - int(s) == 0.0 else -1
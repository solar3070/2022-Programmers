def solution(a, b):
    gcd, lcm = min(a, b), max(a, b)
    while gcd != 0:
        r = lcm % gcd
        lcm, gcd = gcd, r
    answer = [lcm, a * b / lcm]
    return answer
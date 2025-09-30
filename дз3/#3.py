#3
def gcd(m, n):
    n_const = n
    m_const = m
    min1 = 10000 
    min2 = 10000
    while m != n:
        if m > n:
            m = m - n
        else:
            n = n - m
    for x in range(-1000, 1001):
        for y in range(-1000, 1001):
            if x * m_const + y * n_const == n:
                if abs(x) + abs(y) < min1 or ((abs(x) + abs(y)) == min1 and x < min2):
                    min1 = abs(x) + abs(y)
                    min2 = x
                    c = []
                    c.append(x)
                    c.append(y)
    return *c, n


a, b = map(int, input().split())


print(*gcd(a, b))
#2
def simple(n):
    a = []
    i = 0
    if n == 0:
        a.append('0')
        return a
    else:
        while i <= n:
            i += 1
            if n % i == 0:
                a.append(i)
                n //= i
                i = 1
        return a

x = int(input())
print(*simple(x), sep = '*')
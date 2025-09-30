#4
def triangle(n1, s1):
    a = []
    if n1 % 2 != 0:
        for i in range(1, n1//2 + 2):
            a.append(s1*i)
        for j in range(n1//2, 0, -1):
            a.append(s1*j)
    else:
        for i in range(1, n1//2 + 1):
            a.append(s1*i)
        for j in range(n1//2, 0, -1):
            a.append(s1*j)
    return a

n = int(input())
s = input()

print(*triangle(n, s), sep = '\n')

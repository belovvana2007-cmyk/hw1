#1
def fib(n):
    if n <= 1:
        return n
    else:
        a = 1
        b = 0
        for i in range(n-1):
            a, b = a+b, a
        return(a)
    
n = int(input())

print(fib(n))
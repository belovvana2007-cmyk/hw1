#8
n = int(input())
a = list(map(int, input().split()))

sr = sum(a)//n
min = 1000000

for i in range(len(a)):
    if abs(sr - a[i]) < min:
        min = abs(sr - a[i])
        res = a[i]
print(res)

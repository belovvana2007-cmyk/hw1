#7
a = list(map(int, input().split()))
max = 0
res = 0
for i in range(len(a)):
    if a.count(a[i]) > max:
        max = a.count(a[i])
        res = a[i]
print(res)

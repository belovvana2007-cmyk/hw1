#6
a = list(map(int, input().split()))
s = []
for i in range(len(a)):
    if a.count(a[i]) == 1:
        print(a[i], end = ' ')
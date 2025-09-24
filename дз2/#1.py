#1
a = list(map(int, input().split()))
s = 0.5 * (a[0]) * (a[0] + 1)
print(int(s - sum(a) + a[0]))

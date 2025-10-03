#8
a = input().split()
b = input().split()

res_1_a = set(a) - set(b)
res_1_b = set(b) - set(a)

res_2 = set(a) ^ set(b)

res_3 = set(a) & set(b)

print(res_1_a, res_1_b, res_2, res_3)
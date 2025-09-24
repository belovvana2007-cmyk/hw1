#2
G, s = input().split()
len_g = len(s) // int(G)
a = ''
for i in range (0, len(s), len_g):
    a += s[i:i+len_g][::-1]
print(a)

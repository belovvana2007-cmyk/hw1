#9
f = open('C:/Users/User/Desktop/input.txt')
s = f.read()

signs = '.!?'

k = 0

for i in range(len(s)-1):
    if str(s[i]) in signs:
        k += 1
        if s[i+1] in signs:
            k -= 1
print(k+1)

#10
f = open('C:/Users/User/Desktop/input.txt', encoding='utf-8')
s = f.read()

i = 0

lat = 'аеёиоуыэюя'
res = ''

while i < len(s):
    res += s[i]
    if s[i] in lat:
        if ((i == 0) or (i > 0 and s[i - 1] not in lat)) and ((i == len(s) - 1) or (i < len(s) - 1 and s[i + 1] not in lat)):
            res += 'с' + s[i] 
    i += 1
print(res)



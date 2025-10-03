#7
f = open('C:/Users/User/Desktop/qwerty.txt')
s = f.read()

signs = '.,!?-()'
for i in signs:
  s = s.replace(i, ' ')
s_new = set(s.lower().split())

a = {}
k = 0

for i in s.lower().split():
  if i in a:
    a[i] += 1
  else:
    a[i] = 1

while k != 10:
  print(max(a, key = a.get), a[max(a, key = a.get)])
  del a[max(a, key = a.get)]
  k += 1
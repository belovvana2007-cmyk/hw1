#3
s = input().strip()

pal_const = 1
mir_const = 1
pal = 'AHIMOTUVWXY18'

for i in range(len(s) // 2):
    if s[i] != s[len(s) - i - 1]:
        pal_const = 0

for i in range(len(s) // 2 + 1):
    l = s[i]
    r = s[len(s) - i - 1]
    if l in pal:
        if l != r:
            mir_const = 0
    elif l == 'E':
        if r != '3':
            mir_const = 0
    elif l == '3':
        if r != 'E':
            mir_const = 0
    elif l == 'J':
        if r != 'L':
            mir_const = 0
    elif l == 'L':
        if r != 'J':
            mir_const = 0
    elif l == 'S':
        if r != '2':
            mir_const = 0
    elif l == '2':
        if r != 'S':
            mir_const = 0
    elif l == 'Z':
        if r != '5':
            mir_const = 0
    elif l == '5':
        if r != 'Z':
            mir_const = 0
    else:
        mir_const = 0

if pal_const == 1 and mir_const == 1:
    print(s, "is a mirrored palindrome.")
elif pal_const == 1:
    print(s, "is a regular palindrome.")
elif mir_const == 1:
    print(s , "is a mirrored string.")
else:
    print(s, "is not a palindrome.")




























#6
import numpy as np

def mnk(a, b, c):
    n = np.polyfit(a, b, c)
    return n

x = np.array(list(map(float, input().split())))
y = np.array(list(map(float, input().split())))
z = int(input())

print(mnk(x, y, z))
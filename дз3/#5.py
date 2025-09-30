#5
import numpy as np

def spiral(N, M):
    left, top, bottom, right = 0, 0, N, M
    res = np.zeros((N, M))

    num = 1

    while left < right and top < bottom:
        res[top, left:right] = np.arange(num, num + right - left)
        num += right - left
        top += 1

        res[top:bottom, right - 1] = np.arange(num, num + bottom - top)
        num += bottom - top
        right -= 1

        if not (left < right and top < bottom):
            break

        res[bottom - 1, left:right][::-1] = np.arange(num, num + right - left)
        num += right - left
        bottom -= 1

        res[top: bottom, left][::-1] = np.arange(num, num + bottom - top)
        num += bottom - top
        left += 1

    return res

x, y = map(int, input().split())
a = spiral(x, y)
for i in range(x):
    print([int(x * (i + 1)) for x in a[i]])
#7
import numpy as np

n, m = map(int, input().split())
a = []

for i in range(n):
  s = list(map(int, input().split()))
  a.append(s)

matrix = np.array(a)
delta = int(np.linalg.det(matrix.T[0:m-1].T))

for j in range(m+1):

  matrix_const = matrix.T[0:m-1].T.copy()
  matrix_const[:, j] = matrix[:, m-1]
  
  delta_1 = int(np.linalg.det(matrix_const))
  x = delta_1 / delta
  
  print(int(x))
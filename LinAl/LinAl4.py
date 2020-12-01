import numpy as np
A = np.array([[1, 2, 1], [3, -5, 3], [2, 7, -1]])
det = np.linalg.det(A)
rank = np.linalg.matrix_rank(A)

print(f'№4\n'
      f'Определитель матрицы = {det}\n'
      f'Ранг матрицы = {rank}')

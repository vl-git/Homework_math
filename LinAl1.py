import numpy as np

a = np.array([[3, -12, 5], [7, 4, -2], [5, -3, -4]])
b = np.array([3, -5, -4])

x, y, z = np.linalg.solve(a, b)
print(f'№ 1\n'
      f'x = {x}\n'
      f'y = {y}\n'
      f'z = {z}')
print()


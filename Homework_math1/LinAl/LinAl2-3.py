import numpy as np
x = [1, 8, 12]
y = [0, -1, 5]

vec = np.cross(x, y)
sca = np.dot(x, y)

print(f'№2\n'
      f'Скалярное произведение векторов: {sca}\n'
      f'Векторное произведение векторов {vec}')
print()

absx = np.linalg.norm(x)
absy = np.linalg.norm(y)
cos = sca / (absx * absy)
angle = np.arccos(cos)

print(f'№3\n'
      f'Абсолютное значение x = {absx}\n'
      f'Абсолютное значение y = {absy}\n'
      f'Угол между векторами = {angle}')
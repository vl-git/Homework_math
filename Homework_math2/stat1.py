import numpy as np
from sklearn.linear_model import LinearRegression
s = np.array([76.92, 76.25, 75.98, 76.26, 76.01, 75.76])
e = np.array([91.17, 90.39, 90.23, 90.35, 90.26, 89.94])

mean_s = np.mean(s)
median_s = np.median(s)
var_s = np.var(s)
std_s = np.std(s)
print(f'Dollar:\n'
      f'Mean = {mean_s}\n'
      f'Median = {median_s}\n'
      f'Var = {var_s}\n'
      f'Std = {std_s} \n')

mean_e = np.mean(e)
median_e = np.median(e)
var_e = np.var(e)
std_e = np.std(e)
print(f'Euro:\n'
      f'Mean = {mean_e}\n'
      f'Median = {median_e}\n'
      f'Var = {var_e}\n'
      f'Std = {std_e} \n')

cov_se = np.cov(s, e)[0][1]
print(f'Ковариация s_e = {cov_se}')

R = np.corrcoef(s, e)[0][1]
print(f'Коэффициент корреляции (R Пирсона) = {R}\n')

s = s.reshape((-1, 1))
model = LinearRegression()
model.fit(s, e)
r_sq = model.score(s, e)
B = model.intercept_
A = model.coef_[0]
print(f'Linear regression:\n'
      f'e = {A} * s + {B} ')




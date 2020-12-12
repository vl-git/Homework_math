from scipy.stats import uniform
set = uniform.rvs(-3, 6, size=10000)
print('x равномерно распределена на интервале (-3, 3)', end='\n')
print(f'Prob x < 1 = {uniform.cdf(1, loc=-3, scale=6)}\n'
      f'Prob |x| < 1 = {uniform.cdf(1, loc=-3, scale=6) - uniform.cdf(-1, loc=-3, scale=6)}\n'
      f'Prob x < 3 = {uniform.cdf(3, loc=-3, scale=6)}\n'
      f'Prob |x| < 3 = {uniform.cdf(3, loc=-3, scale=6) - uniform.cdf(-3, loc=-3, scale=6)}\n')

print(f'Квантили распределения:\n'
      f'Q50 = {uniform.ppf(0.5, loc=-3, scale=6)}\n'
      f'Q90 = {uniform.ppf(0.9, loc=-3, scale=6)}\n'
      f'Q99 = {uniform.ppf(0.99, loc=-3, scale=6)}')
from scipy.stats import norm
import scipy.stats as st
import numpy as np
print(f'Prob x < 1 = {norm.cdf(1)}\n'
      f'Prob |x| < 1 = {norm.cdf(1) - norm.cdf(-1)}\n'
      f'Prob x < 3 = {norm.cdf(3)}\n'
      f'Prob |x| < 3 = {norm.cdf(3) - norm.cdf(-3)}\n')

set = np.random.normal(size=10000)
q50 = st.scoreatpercentile(set, 50)
q99 = st.scoreatpercentile(set, 99)
q90 = st.scoreatpercentile(set, 90)
print(f'On random dataset of 10000 values with normal variable:\n'
      f'Q50 = {q50}\n'
      f'Q90 = {q90}\n'
      f'Q99 = {q99}\n')

print(f'Theoretically:\n'
      f'Quantile 50 = {norm.ppf(0.5)}\n'
      f'Quantile 90 = {norm.ppf(0.9) - norm.cdf(-1)}\n'
      f'Quantile 99 = {norm.ppf(0.99)}\n')
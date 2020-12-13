import numpy as np
import matplotlib.pyplot as plt
dice1 = np.random.randint(1, 7, 10000)
dice2 = np.random.randint(1, 7, 10000)
dice3 = np.random.randint(1, 7, 10000)
dataset = []
for pos, v in enumerate(dice1):
    dataset.append(v + dice2[pos] + dice3[pos])

freq = {}
for val in dataset:
    freq[val] = dataset.count(val)

prob = {}
for k, v in freq.items():
    prob[k] = v / len(dataset)

prob_s = sorted(prob)
probability = {val: prob[val] for val in prob_s}
print(f'Вероятность того, что сумма граней трех кубиков равна 3: {probability[3]}\n'
      f'Вероятность того, что сумма граней трех кубиков равна 4: {probability[4]}')

fig, ax = plt.subplots()

ax.plot(probability.keys(), probability.values(), 'o')
ax.grid()
ax.set_xlabel('Сумма значений, выпавших на трех кубиках')
ax.set_ylabel('Вероятность выпадения')

plt.show()

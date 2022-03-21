from scipy.stats import norm, t
import pandas as pd
import numpy as np

alpha = 0.3

df = pd.read_csv('watermelon_20.csv', header=None)
n = df.shape[0]
mean = np.mean(df)
var = np.var(df)


left_border = mean - t.ppf(1 - alpha/2, n-1) * var/n**0.5
right_border = mean + t.ppf(1 - alpha/2, n-1) * var/n**0.5
print(float(left_border), float(right_border))

#Ответ: да



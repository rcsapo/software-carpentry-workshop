%matplotlib inline

import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

data = pd.read_csv('A2_mosquito_data.csv')
data['temperature'] = (data['temperature'] - 32) * 5 / 9.0
regr_results = sm.OLS.from_formula('mosquitos ~ temperature + rainfall', data).fit()
parameters = regr_results.params
predicted = parameters[0] + parameters[1] * data['temperature'] + parameters[2] * data['rainfall']
plt.plot(predicted, data['mosquitos'], 'ro')
min_mosquitos, max_mosquitos = min(data['mosquitos']), max(data['mosquitos'])
plt.plot([min_mosquitos, max_mosquitos], [min_mosquitos, max_mosquitos], 'k-')
print parameters
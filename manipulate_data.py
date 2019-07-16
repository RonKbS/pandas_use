import pandas


data = pandas.read_csv('brain_size.csv', sep=';', na_values=".")
# print(data)

# pandas dataframe can be seen as dictionary of 1D series eg arrays or lists
import numpy as np
t = np.linspace(-6, 6, 20)
sin_t = np.sin(t)
cos_t = np.cos(t)
# print(pandas.DataFrame({'t': t, 'sin': sin_t, 'cos': cos_t}))

# to manipulate data
# print(data.shape)
# print(data.columns)
# print(data['Gender'])

# Simpler selector
# print(data[data['Gender'] == 'Female']['VIQ'].mean())

# return count, mean, std, min, max, 25%, 50% and 75% percentile
# print(data.describe())

# split dataframe on values of categorical variables
groupby_gender = data.groupby('Gender')
for gender, value in groupby_gender['VIQ']:
    print((gender, value.mean(), value.count()))

for gender, value in groupby_gender['VIQ']:
    print(gender, value)

import pandas as pd
import numpy as np

data = pd.read_csv('acs2015_census_tract_data.csv')
print(data.head())

# 1) Есть ли такие графства (County) где уровень безработицы нулевой?
# print(data[data['Unemployment'] == 0]['County'].unique())

# 2) У какого штата наименьший средний уровень безработицы (используйте колонку `Unemployment` и метод **.mean()** ) ? 

group = data[['State','Unemployment']].groupby('State').agg('mean')
print(group[group.min()['Unemployment'] == group['Unemployment']])

# 3) Какой наибольший средний уровень дохода (используйте колонку `Income` и метод **.mean()** ) среди штатов?

print(data[['State','Income']].groupby('State').agg('mean').max())

# 4) В каком штате самое большое население женщин среди штатов?
group = data[['State','Women']].groupby('State').agg('sum')
print(group[group.max()['Women'] == group['Women']])

# 5) В каком штате мужчин больше чем женщин и на сколько процентов?
# x = lambda x : x[0] - x[1]
# dif = data[['State','Men','Women']].groupby('State').agg(x)
# print(dif.head())


# print(group[group.max()['Women'] == group['Women']])
fm = data[['State','Men','Women']].groupby('State').agg('sum')
# print(fm.head())
fm['dif'] = fm['Men']-fm['Women']
fm['%'] = (fm['Men']-fm['Women'])/(fm['Men']+fm['Women']) * 100
# print(fm.head())
print(fm[fm['dif']>0]['%'])
# print(fm[fm['dif']>0]['State'])
# print(x['State'])
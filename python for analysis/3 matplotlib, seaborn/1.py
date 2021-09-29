import matplotlib
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

# Нарисуйте с помощью функции plot:

# (√x)  — штриховая (dashed) линия с точками в форме ромбов (diamond) зелёного (green) цвета.
# (√4x)  — пунктирная (dotted) линия с точками в форме крестиков (x marker) пурпурного (magenta) цвета.
# Используйте для этого документацию по функции plot.

# x = np.linspace(0, 16, 20)
# plt.plot(x, x**(1/2), 'D--g')
# plt.plot(x, x**(1/4), 'x:m')
# plt.show()

# /////////////////////////////////////////////////
# Отфильтруйте данные, оставив только информацию по 2014 году.
# Используйте эти данные и код из урока для того, чтобы нарисовать график цен на акции компании Tesla в 2014 году.
# Представьте, что акции были куплены на уровне 250$ и теперь интересно увидеть, как часто цена поднималась выше этого порога.
# Попробуйте придумать, как автоматически вычислить явно заданные числа 0 и 300 при задании yticks.
# Даты рисовать не обязательно, но вы можете изобразить те, что кажутся вам важными :)
# tesla = pd.read_csv('Tesla.csv', parse_dates=True, index_col='Date')
# buy_price = 250

# tesla = tesla[tesla.index.year == 2014]
# max_p_date = tesla[tesla['High']==tesla['High'].max()].index
# min_p = int(round(tesla['Low'].min(), -1))-10
# # print(tesla['Low'].min())
# max_p = int(round(tesla['High'].max(), -1))+10
# plt.figure(figsize=(18,10))
# high_prices_line, = plt.plot(tesla.index, tesla['High'], label='High', color='g')
# low_prices_line, = plt.plot(tesla.index, tesla['Low'], label='Low', color='r')
# plt.setp([high_prices_line, low_prices_line], linewidth=0.5, alpha=0.5)
# plt.axhline(y=buy_price, ls='--', label=f'Buy price {buy_price}$')
# plt.axvline(x=max_p_date, ls='--', color='y', label=max_p_date[0])
# plt.xlabel('Dates')
# plt.ylabel('Stock prices, US$')
# plt.grid()
# plt.yticks(range(min_p, max_p, 10), labels=range(min_p, max_p, 10))
# plt.legend(loc='lower right', title='Legend')
# plt.title('Tesla stock prices')
# plt.show()
# print(tesla.head())
# ///////////////////////////////
# data = pd.read_csv('AB_NYC_2019.csv')

# data.drop(['id', 'name', 'host_name', 'last_review'], axis=1, inplace=True)
# data.fillna({'reviews_per_month':0},inplace=True)
# # print(data.head()) 
# print(data.info())
# colors = matplotlib.colors.get_named_colors_mapping()
# color_map={
#     'Brooklyn': colors['xkcd:cloudy blue'],
#     'Manhattan': colors['xkcd:azul'], 
#     'Queens': colors['xkcd:electric lime'], 
#     'Staten Island': colors['xkcd:fresh green'], 
#     'Bronx': colors['xkcd:warm purple']
# }
# plt.figure(figsize = (10,5))
# for name, group in data.groupby('neighbourhood_group'):
#     plt.scatter(group['longitude'],group['latitude'], s=0.1, c=color_map[name], label = name)
# plt.xlabel('longitude')
# plt.ylabel('latitude')
# plt.legend(markerscale=10)
# plt.title('Accomodation location by neighbourhood_group')
# plt.show()
# print('1')
# //////////////
# room_size = data.groupby('room_type').size()
# plt.bar(room_size.index, room_size.values)
# plt.xlabel('Room types')
# plt.ylabel('Room quantity')
# plt.title('Accomodation types in numbers')
# plt.show()
# print(room_size)
# ///////////////
# plt.figure(figsize = (10,5))
# x = np.asarray([0,1,2])
# width = 0.15
# i = -2
# for name, group in data.groupby(['neighbourhood_group']):
#     plt.bar(x-i*width, group.groupby('room_type').size().values, width, label = name)
#     print(x-i*width)
#     print(group.groupby('room_type').size().values)
#     i+=1
# plt.title('Accomodation types in numbers by neighbourhood_group')
# plt.xticks(x,list(data.groupby('room_type').groups.keys()))
# plt.legend()
# plt.show()
# /////////////////////////////////////////////////

# C помощью первого способа и автоматической расстановки цвета постройте такой же график с помощью функции scatter, как на уроке, 
# сгруппировав данные по колонке neighbourhood (мы использовали в примере neighbourhood_group).
# C помощью одного вызова функции scatter постройте точки по координатам, использовав при этом в качестве цвета колонку availability_365, 
# для отображения соответствия цвета значения используйте функцию colorbar.
# Используйте пример из урока по функции bar и измените группировку: покажите количество жилья разных типов по административному округу 
# (neighbourhood_group).
# Повторите то же самое, что делали на уроке с hist, для number_reviews.
# Используйте boxplot для визуализации распределения number_reviews по neighbourhood_group.
# print(data.head())
# for name, group in data.groupby(['neighbourhood']):
#     plt.scatter(group['longitude'],group['latitude'],s=0.05, label=name)
# plt.xlabel('longitude')
# plt.ylabel('latitude')
# plt.legend(markerscale = 10)
# plt.title('Accomodation location by neighbourhood')
# plt.show()
# //////////////////////////////
# plt.figure(figsize=(10,5))
# plt.scatter(data['longitude'], data['latitude'], s=0.05, c = data['availability_365'])
# plt.xlabel('longitude')
# plt.ylabel('latitude')
# plt.colorbar()
# plt.title('Accomodation location by year availability')
# plt.show()
# /////////////////////////////////
# plt.figure(figsize = (10,5))
# x = np.asarray([0,1,2,3,4])
# width = 0.15
# i = -1
# for name, group in data.groupby(['room_type']):
#     plt.bar(x-i*width, group.groupby('neighbourhood_group').size().values, width, label = name)
#     i+=1
# plt.title('Accomodation neighbourhood_group in numbers by types')
# plt.xticks(x,list(data.groupby('neighbourhood_group').groups.keys()))
# plt.legend()
# plt.show()
# /////////////////////////////////////////
# plt.figure(figsize=(8, 8))
# filtered_data = data[data['number_of_reviews'] > 20]
# for name, group in filtered_data.groupby(['neighbourhood_group']):
#     plt.hist(group['number_of_reviews'], label=name, bins=100, alpha=0.5)
# plt.xlabel('Number of reviews, psc')
# plt.ylabel('Accomodation quantity')
# plt.title('Number of reviews by neighbourhood_group')
# plt.legend()
# plt.show()
# ////////////////////////////////////////
# Используйте boxplot для визуализации распределения number_reviews по neighbourhood_group.
# plt.figure(figsize=(8, 8))
# index = 1
# for name, group in data.groupby(['neighbourhood_group']):
#     plt.boxplot(group['number_of_reviews'], positions=[index], labels=[name])
#     index += 1
# plt.xlabel('neighbourhood_group')
# plt.ylabel('number_of_reviews')
# plt.title('Number of reviews by neighbourhood_group')
# plt.show()
# /////////////////////////////////////////////
# Постройте с помощью subplots графики цены для датасета aws spot prices для ОС Windows и всех архитектур вида i*. 
# *Обратите внимание на то, какой лучше сделать период между датами для удобного отображения. 
# data = pd.read_csv('ap-northeast-1.csv')
# print(data.info())
# print(data.head())
# fig, axes = plt.subplots(1,2)
# axes[0].plot(list(data.groupby('OS').groups.keys()),data.groupby('OS').mean('price'),label = 'price by OS')
# plt.xlabel = 'OS'
# plt.ylabel = 'mean price'
# axes[1].plot(list(data.groupby('something_else').groups.keys()),data.groupby('something_else').sum('price'), label = 'price by something')
# plt.xlabel = 'something_else'
# plt.ylabel = 'mean price'
# plt.show()
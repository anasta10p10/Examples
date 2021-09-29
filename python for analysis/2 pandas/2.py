# Практическая часть домашнего задания на этой неделе будет довольно объемным: 

# 1) Нужно поиграться с ноутбуком и подкрутить скрипт для подобного отчета **по долларам США** и еще одной валюте на выбор. 
# Смело копируйте этот ноутбук и сделайте так, чтобы **отчет о транзакциях** был **в одном файле экселя** и пошлите себе **файлик 
# на почту**.<br>

# 2) Отток мы посчитали, как на счет посчитать retention? Или сколько пользователей в текущем месяце присутствуют в прошлом месяце. 
# (по сути это ***обратная*** или ***инвертированная задача*** для той что уже мы посчитали.)

# 3) И свободная часть: **реализовать похожий скрипт для своих нужд** и со своими данными.

# /////////////////////////////////////////////////////////////////////////
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# import openpyxl

data = pd.read_csv('data.csv.gz', compression='gzip')

# преобразование даты
data['period'] = pd.to_datetime(data['period'], format='%d/%m/%Y')

# преобразование времени
data['transac_time'] = data['trdatetime'].str[-8:]

# разные компоненты даты по столбцам
data['transac_day'] = data['trdatetime'].str[:2]
month_dict={'JAN':'01', 'FEB':'02', 'MAR':'03', 'APR':'04', 'MAY':'05', 'JUN':'06', 
            'JUL':'07', 'AUG':'08', 'SEP':'09', 'OCT':'10', 'NOV':'11', 'DEC':'12'}
data['transac_month'] = data['trdatetime'].str[2:5].map(month_dict)
data['transac_year'] = '20'+data['trdatetime'].str[5:7]

# комбинированное поле месяц-год
#data['transac_year_month'] = data['period'].apply(lambda x: x.strftime('%m-%Y')) 
data['transac_year_month'] = '20'+data['trdatetime'].str[5:7]+'-'+data['trdatetime'].str[2:5].map(month_dict)

# x= data.groupby('currency')['amount'].agg(['min', 'mean', 'median','max']).tail()

wiki_table = pd.read_csv('currency_codes_wiki.csv')

wiki_table = wiki_table.append({'num_code': 810, 'currency_code':'RUR','title':'Russian ruble'},ignore_index=True)
data = data.merge(wiki_table, left_on='currency', right_on='num_code', how='left')

mcc = pd.read_excel('mcc_codes.xls',skiprows=1)
mcc = mcc.iloc[:,:-1]
mcc = mcc.rename(columns={'MCC CODE':'mcc','Program Type:':'category'})
data = data.merge(mcc, on='mcc', how='left')
# //////////////////////////////////////////////////////
# Отчет по средним тратам.
# .......................................

# def do_report(dataframe, currency_int): 
#     report = pd.DataFrame()
#     currency = currency_int
#     df = dataframe[dataframe['currency'] == currency]
#     dates = sorted(df['transac_year_month'].unique())


#     for date in dates:
#         buffer = df[df['transac_year_month'] == date][['transac_year_month','amount','category']].set_index(['transac_year_month','category'])

#         # посчитаем значения квартилей по которым будем обрезать наши значния в транзакциях
#         low = .05
#         high = .95
#         quant_df = buffer.quantile([low, high])

#         # отфильтруем значения 
#         filtered_df = buffer.apply(lambda x: x[(x>quant_df.loc[low,x.name]) & (x < quant_df.loc[high,x.name])], axis=0)
#         filtered_df = filtered_df.reset_index().groupby(['transac_year_month','category']).mean()

#         # объединяем посчитанную таблицу с главной
#         report = pd.concat([report, filtered_df])

#     # разворачиваем  таблицу, транспонируем и удаляем одну колонку по которой индексировались - непростое комбо!
#     report = report.unstack().T
#     """
#     if report.shape[0] == 0: # сравниваем длину нашего отчета с нулем. если да, то делаем операции внутри цикла.
        
#         report = pd.DataFrame() # обнуляем наш отчет
        
#         # для каждой из дат считаем все теже операции, что и выше, но без отсечения выбросов.
#         for date in dates:
#             buffer = df[df['transac_year_month'] == date][['transac_year_month','amount','category']].set_index(['transac_year_month','category'])
#             buffer = buffer.groupby(['transac_year_month','category']).mean()
#             report = pd.concat([report, buffer])
#             return round(report,2) # возвращаем таблицу с округленными значениями
#     else:
#         return round(report,2)
# .....................
# Записать в файл
# ...................
# def write_excel_cyclicaly(dataframe, dataframe_name):
#     import openpyxl
#     """
#     Эта функция циклично добавляет табличку на новыый лист с названием этой таблицы, используя конструкцию with.
    
#     """

#     with pd.ExcelWriter('report.xlsx', engine='openpyxl') as writer:
#         writer.book = book
#         writer.sheets = dict((ws.title, ws) for ws in book.worksheets)    

#         dataframe.to_excel(writer, f'{dataframe_name}')
#         writer.save()
# cur = 840
# trx_cats = data[data['currency'] == cur]['trx_category'].unique()

# # создаем/инициализируем файл 
# import openpyxl
# # filepath = "../data/mean_check/results/"
# book = openpyxl.Workbook()
# book.save('report.xlsx')

# # print(do_report(data[data['trx_category'] == 'POS'],810))
# # цикл создания отчетов и записи в эксель файл
# for trx_cat in trx_cats:
#     report = do_report(data[data['trx_category'] == trx_cat], cur)
#     print(report)
#     write_excel_cyclicaly(report, f'{trx_cat}')
#     # print(f'ghdbnf{trx_cat}')

# /////////////////////////////////////////////////////////////////
# Отчет по оттоку.
# ......................
# churn_array = []

# for month in sorted(data['transac_year_month'].unique()):
#     # 1
#     try:
#         # 2
#         current = data[data['transac_year_month'] == month]['cl_id'].unique()
#         # 3
#         churned_idx = np.isin(current, previous, invert=True) 
#         # 4
#         churned = current[churned_idx] 
#         # 5
#         churn_array.append(len(churned))
#         # 6
#         previous = current
#     except NameError:
#         churn_array.append(np.nan)
#         # 7
#         previous = data[data['transac_year_month'] == month]['cl_id'].unique()

# churn_table = pd.DataFrame({'months':sorted(data['transac_year_month'].unique()),
#                             'churn':churn_array
#                            }, columns=['months','churn'])
# churn_table.to_csv('results/churn.csv',index=False)
# тток мы посчитали, как на счет посчитать retention? Или сколько пользователей в текущем месяце присутствуют в прошлом месяце. 
# (по сути это ***обратная*** или ***инвертированная задача*** для той что уже мы посчитали.)
dat = data[['cl_id','transac_year_month']]
date = dat['transac_year_month'].unique()
dat.set_index('cl_id', inplace=True)
dat['DateGroup'] = dat.groupby(level=0)['transac_year_month'].agg('min')
dat.reset_index(inplace=True)
grouped = dat.groupby(['transac_year_month', 'DateGroup']).agg({'cl_id': pd.Series.nunique})
ret = grouped.unstack(0)
print(ret.head())

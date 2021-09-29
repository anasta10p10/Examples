# Генератор текста может показать несколько пробелов подряд. Запретить быть выведенными нескольким 
# пробелам подряд
# import zipfile
# import os
# file_name = os.path.join("data","bratya-karamazovy.zip")
# zip = zipfile.ZipFile(file_name,"r")
# file_name = zip.extract(zip.namelist()[0], "data")
# import chardet
# import pprint
# import string
# rawdata = open(file_name, "rb").read()
# result = chardet.detect(rawdata)
# charenc = result['encoding']
# print(charenc)

# accuracy = 8
# cur_string = ' '*accuracy
# occurencies = {}
# with open (file_name, mode="r", encoding=charenc) as file:
#     for line in file:
#         for char in line[:-1]:
#             if char.lower() not in string.ascii_lowercase:
#                 if cur_string in occurencies:
#                     if char in occurencies[cur_string]:
#                         occurencies[cur_string][char]+=1
#                     else:
#                         occurencies[cur_string][char]=1
#                 else:
#                     occurencies[cur_string]={char:1}
#                 cur_string = cur_string[1::]+char

# total = {}
# generate ={}
# for cur_char, char_info in occurencies.items():
#     total[cur_char]=sum(char_info.values())
#     generate[cur_char] = []
#     for char, count in char_info.items():
#         generate[cur_char].append([count, char])
#     generate[cur_char].sort(reverse=True)  

# import random 

# n=10000
# # i=0
# cur_string = ' '*accuracy
# for i in range(n):
#     char_info_elem = generate[cur_string]
#     random_number = random.randint(1, total[cur_string])
#     pos = 0
#     for count, char in char_info_elem:
#         pos += count
#         if char==' ' and cur_string[-1]==' ':
#             pass
#         elif random_number <= pos:
#             print(char, end="")
#             break
#     cur_string = cur_string[1::]+char
# /////////////////////////////////////////////////////////
# Подсчитать количество вхождений каждой буквы в произведении Братья Карамазовы.
#
# Вывести результат в виде:
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу

# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# .....................................
# import zipfile
# import os
# file_name = os.path.join("data","bratya-karamazovy.zip")
# zip = zipfile.ZipFile(file_name,"r")
# file_name = zip.extract(zip.namelist()[0], "data")
# import chardet
# rawdata = open(file_name, "rb").read()
# result = chardet.detect(rawdata)
# charenc = result['encoding']
# mas={}
# with open (file_name, mode="r", encoding=charenc) as file:
#     for line in file:
#         for char in line[:-1]:
#             if char in mas:
#                 mas[char]+=1
#             else:
#                 mas[char]=1

# list1=[]
# for key,value in mas.items():
#     list1.append([value, key])
# list1.sort(reverse=True)
# print('+---------+----------+')
# print('|  буква  | частота  |')
# print('+---------+----------+')
# sum1=0
# for value, key in list1:
#     sum1+=value
#     print(f'|{key:^9}|{value:^10}|')
# print('+---------+----------+')
# print(f'|  итого  |{sum1:^10}|')
# print('+---------+----------+')
# ///////////////////////////////////////////////////////////////////////
# Дан файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой текстовый файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#

# Далее нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
import os
file_name = os.path.join("data","events.txt")
file_output_name = os.path.join("data", "result.txt")
min1={}
with open(file_name, 'r') as file:
    for line in file:
        if "NOK" in line:
            if line[1:17] in min1:
                min1[line[1:17]]+=1
            else:
                min1[line[1:17]]=1
with open(file_output_name, mode="w") as file1:
    for i,j in min1.items():
        file1.write(f'[{i}] {j}\n')
# with open(file_output_name, 'r') as file1:
#     for line in file1:
#         print(line)








#             with open(file_output_name, mode="a") as file1:
#                 file1.write(line)
# with open(file_output_name, mode="r") as file1:
#     with_not=file1.read()
#     print(with_not)
# for line in with_not:


# Для написанной игры Быки и коровы добавить обработчики различных исключений
# import sys

# # pl1=input('Игрок 1 - Тайное число: Введите 4-значное число без повторения цифр')
# # pl2=input('Игрок 2 - Тайное число: Введите 4-значное число без повторения цифр')
# players={'Игрок 1':input('Игрок 1 - Тайное число: Введите 4-значное число без повторения цифр'), 
# 'Игрок 2': input('Игрок 2 - Тайное число: Введите 4-значное число без повторения цифр')}
# t=True
# while True:
#     for i in players:
#         if len(players[i])==4 and len(set(players[i]))==4 and players[i].isdigit()==True:
#             t=False
#             pass
#         else:
#             players[i]=input(f'{i} : Вы ввели не подходящее число.Введите 4-значное число без повторения цифр')  
#     if not t:
#         break
# x=0
# pos_var={'Игрок 1':0,'Игрок 2':0}
# def prov(p,n,pl): #где p-чей ход, п-число на проверку, pl - проверка для какого игрока
#     b=0
#     k=0
# # try:
#     for i in range(len(n)):
#         if pl[i]==n[i]:
#             b+=1
#         elif n[i] in pl:
#             k+=1
#     if b==4:
#         x="Точное попадание!"
#         pos_var[p]=x
#         print(x)
#         return x
#     x= f'Результат: {k} «коров(ы)» и {b} «бык(ов)»'
#     print(x)
#     pos_var[p]=x
# # except:
# #     if len(n)>4 or len(n)<4:
# #         print('Неверно указано число на проверку. ВВодить нужно 4 х-значное число. Попробуйте еще раз')
# #         prov(p,input('Введите другое число'),pl)
# #     else:
# #         print('Неизвестная ошибка')
# #         sys.exit()
# # finally:
# #     print('Игра не может продолжаться')
# #     sys.exit()
     
# t = True
# while True:
#     if  "Точное попадание!" not in pos_var.values():
#         prov('Игрок 1',input("Введите 4-значное число без повторения цифр"),players['Игрок 2'])
#         prov('Игрок 2',input("Введите 4-значное число без повторения цифр"),players['Игрок 1'])
#     elif pos_var['Игрок 1']=="Точное попадание!" and pos_var['Игрок 2']=="Точное попадание!":
#         print("Ничья")
#         break
#     else:
#         for i in pos_var:
#             if pos_var[i]=="Точное попадание!":
#                 print(f'{players[i]}, Вы победили!!!')
#                 t=False
#                 break
         
#         if not t:
#             break
# ////////////////////////////////////////
# Дан список. Найти сумму его элементов с помощью рекурсии
# ...........................................
# def summa(mas):
#     if len(mas)==0:
#         return 0
#     return mas[0]+summa(mas[1:])
# print(summa([1,2,3,5]))
# /////////////////////////////////////////////
# Реализовать 4 функции для подсчета значения факторила числа.

# Итеративная
# Рекурсивная
# С помощью декоратора для мемоизации
# Без декоратора, но с мемоизацией (реализовать ее самостоятельно)
# Проверить время выполнения функций на большом наборе данных. Сравнить результаты
# ......................
# Итеративная
# def fact(n):
#     x=1
#     for i in range(2,n+1):
#         x*=i
#     return x
# print(fact(5))
# Рекурсивная
# def fact(n):
#     if n==0:
#         return 1
#     return n*fact(n-1)
# print(fact(5))
# С помощью декоратора для мемоизации
import time
import random
# s=time.time()
# from functools import lru_cache
# @lru_cache
# def fact(n):
#     print(n)
#     if n==0:
#         return 1
#     return n*fact(n-1)

# for i in range(100):
#     s = time.time()
#     r=random.randint(0,100)
#     print(f"f({r})")
#     fact(r)
#     e = time.time()
#     print(e-s)
# Без декоратора, но с мемоизацией (реализовать ее самостоятельно)
# import time
# import random
# slov={0:1,1:1}
# def fact(n):
#     print(n)
#     if n in slov:
#         return slov[n]
#     if n>1:
#         x= n*fact(n-1)
#         slov[n] = x
#         return x
# for i in range(100):
#     s = time.time()
#     r=random.randint(0,100)
#     print(f"f({r})")
#     print(fact(r))
#     e = time.time()
#     print(e-s)
# //////////////////////////////
# You should calculate the expressions deviding them to 2 files. 1 - with  answers. 2 - with errors
# import os
# file_name = os.path.join("data", "calc.txt")
# file_answers = os.path.join("data", "answers.txt")
# file_errors = os.path.join("data", "errors.txt")
# with open(file_name, "r") as file, open(file_errors, mode="w") as file1, open(file_answers, mode="w") as file2:
#     for line in file:
#         try:
#             x = eval(line)
                
#         except:
#             file1.write(line)
#         file2.write(str(x)+'\n')
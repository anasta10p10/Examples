# Для задачи с функцией, считающей кол-во цифр в произведении степеней произвольного числа агрументов и декоратора, 
# считающего время выполнения функции, в декоратор добавить округление времени выполнения функции с точностью precision.
# Таким образом, precision должен передаваться в качестве параметра. В итоге, нужно будет написать функцию,
# принимающую параметры и возвращающую декоратор.
# import time
# import random
# def function_returning_decorator(fn=None, *, precision=5):
#     if fn==None:
#         return lambda fn1: function_returning_decorator(fn1, precision=precision)
#     def wrapper(*args):
#         begin = time.time()
#         res = fn(*args)
        
#         end = time.time()
#         time_answer = round(end - begin, precision)
#         print(time_answer)
#         return(res)
#     return wrapper

# @function_returning_decorator(precision = 5)
# def number_of_digits(*args):
#     res = 1
#     for item in args:
#         temp =  item ** 1000
#         res *= temp
#     return len(str(res))
# n = 100
# arr = [random.randint(1000,3000) for item in range(n)]
# print(number_of_digits(*arr))
# /////////////////////////////////////////////////////////
# Реализовать механизм мемоизации для ЛЮБОЙ функции, т.е. нужно изменять поведение любой передаваемой функции. 
# Например, вычисление факториала или числа Фибоначчи. Определить время выполнения с/без мемоизации для набора случайных чисел.

# Реализовать свою мемоизацию, затем также использовать "встроенный" декоратор functools.lru_cache

# Также добавить к мемоизации измерение времени выполнения. Мемоизацию можно отделить от измерения времени, 
# т.е. применить два декоратора к одной функции, либо не отделять (на ваше усvотрение)

# import time
# import random

# def t(fun):
#     def inner(n):
#         s = time.time()
#         res=fun(n)
#         e = time.time()
#         print(f'Время выполнения -{e-s}')
#         return res
#     return inner


# def memo(f):
#     slov={0:1,1:1}
#     def inner(n):
#         if n not in slov:
#             slov[n]=f(n)
#         return slov[n]
#     return inner


# @memo
# def fact(n):
#     print(n)
#     if n<1:
#         return 1
#     elif n>1:
#         return n*fact(n-1)

# fact_t = t(fact)


# for i in range(100):
#     r=random.randint(0,10)
#     print(f"random is {r}")
#     print(fact_t(r))

# ////////////////////////////////////////

# import time
# import random
# from functools import lru_cache

# @lru_cache
# def fact(n):
#     print(n)
#     if n==0:
#         return 1
#     return n*fact(n-1)

# def t():
#     s = time.time()
#     r=random.randint(0,10)
#     print(f"f({r})", end=' ')
#     print(fact(r))
#     e = time.time()
#     print(e-s)

# for i in range(100):
#     t()
# //////////////////////////////////
# You surely know how range works. You need to create your own my_range that will work as standart range .
# ..............
# def my_range(s=0, n=None, step=1) :
#     if n is None:
#         s, n = 0, s
#     if step==0 or str((n-s)/step)[0]=='-':
#         print('Некорректно заданы исходные данные')
#         return
#     n0=s
#     while True:
#         if n0<n or n0>n:
#             yield n0
#             n0+=step
#         else:
#             return

# for i in my_range(4,4):
#     print(i)
# ///////////////////////////////////////////////
# Create a function getting random number of arguments.
# Find the number of digits in product of all arguments in the power of 1000
# You need to evaluate the time of work of this function
import time
import random

def t(f):
    def res(*args):
        b=time.time()
        r= f(*args)
        print(r)
        e=time.time()
        print(e-b)
    return res

@t
def n(*args):
    res=1
    for item in args:
        temp=item**1000
        res*=temp
    return len(str(res))
k=100
arr= [random.randint(1000,3000) for _ in range(k)]
print(n(*arr))

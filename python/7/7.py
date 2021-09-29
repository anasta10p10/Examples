# You need to calculate the results of calc.txt(in data directory) without using eval.
# create a file with results of calculations containing the operation and the result for it (ex. 3+6=9)
# create a file with wrong operations
# You can use a dictionary of operations as keys (+, -,/, etc) and values containing functions for each operation
# .................................................................
# import os
# file_name = os.path.join("data", "calc.txt")
# file_answers =os.path.join("data", "answers.txt")
# file_errors = os.path.join("data", "errors.txt")
# calc = {
#     "+" : lambda x,y : x+y,
#     "-" : lambda x,y : x-y,
#     "/" : lambda x,y  : x/y,
#     "//" : lambda x,y : x//y,
#     "*" : lambda x,y : x*y,
#     "%" : lambda x,y : x%y
# }

# with open(file_name, "r") as file, open(file_errors, mode="w") as file1, open(file_answers, mode="w") as file2:
#     for line in file:
#         arr = line[:-1].split()
#         try:
#             x = calc[arr[1]](int(arr[0]),int(arr[2]))
#             file2.write(f'{str(line[:-1])} = {str(x)} \n')
#         except:
#             file1.write(str(line))  
# ////////////////////////////////////////////////////////////
#Решить задачу тремя различными инструментами python. На рис "pic".
# ................................................
# from random import randint
# def yp(x1,x2,x3,c):
#     y=x1**2+x2**(0.5)+x3/(x1+x2)+c
#     return y
# for i in range(1000):
#     print(yp(randint(1,5),randint(1,5),randint(1,5),randint(1,5)))

# from functools import partial
# new_yp=partial(yp,x1=5,x3=7)
# for i in range(1000):
#     print(new_yp(x2=randint(1,5),c=randint(1,5)))

# def q(x1):
#     def w(x3):
#         def e(x2):
#             def r(c):
#                 return x1**2+x2**(0.5)+x3/(x1+x2)+c
#             return r
#         return e
#     return w
# yp1=q(5)(7)
# for i in range(1000):   
#     print(yp1(randint(1,5))(randint(1,5)))

# yp2=(lambda x1=5: lambda x3=7: lambda x2: lambda c: x1**2+x2**(0.5)+x3/(x1+x2)+c)
# for i in range(1000):
#     print(yp2()()(randint(1,5))(randint(1,5)))

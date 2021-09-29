# Создать класс Human. Человек имеет имя, возраст, пол, вес. Создать метод, выводящий параметры человека. Создать человека 
# и вывести о нем инфо. Сгенерировать случайным образом список людей. Найти самого молодого человека и вывести инфо о нем.
# .............................................
# class Human:
#     def __init__(self,first_name,second_name,age,gender,weight) -> None:
#         self.first_name=first_name
#         self.second_name=second_name
#         self.age=age
#         self.gender=gender
#         self.weight=weight
#     def show(self):
#         print(self.first_name,self.second_name,self.age,self.gender,self.weight)
    
# human=Human('Michael','Efremov',60,'m',77)
# Human.show(self=human)

# import faker
# from faker import Faker
# fake=Faker()

# import random
# Humans=[]
# for p in range(10):
#     p=Human(fake.first_name(),fake.last_name(),random.randint(0,100), random.randint(0,1),random.randint(0,120))
#     Humans.append(p)
# slov={Humans[0].first_name:Humans[0].age}
# for i in Humans:
    
#     if i.age > max(slov.values()):
#         slov={i.first_name:i.age}
# print(slov)
# //////////////////////////////////////////////////////////////////
# Создать Иерархию классов на основе класса Фигура. Создать классы Треугольник, Прямоугольник, Круг с методами, 
# позволяющими считать периметр и площадь. Создать конструкторы. Создать список разных фигур. Вывести 3 фигуры с самой большой площадью.
# ........................................
# import math
# class Figure():
#     def __init__(self, name):
#         self.name = name
#     def show(self):
#         print(self.name)
#     def S(self):
#         return 0
#     def P(self):
#         return 0
# class Circle(Figure):
#     def __init__(self, name, r):
#         super().__init__(name)
#         self.r = r
#     def show(self):
#         super().show()
#         print(self.r)
#     def S(self):
#         return 3.14 * self.r**2
#     def P(self):
#         return 2 *3.14 *self.r
# class Rectangle(Figure):
#     def __init__(self, name, a,b):
#         super().__init__(name)
#         self.a = a
#         self.b = b
#     def show(self):
#         super().show()
#         print(self.a, self.b)
#     def S(self):
#         return self.a * self.b
#     def P(self):
#         return (self.a + self.b)
# class Triangle(Figure):
#     def __init__(self, name, a,b,c):
#         super().__init__(name)
#         self.a = a
#         self.b = b
#         self.c = c
#     def show(self):
#         super().show()
#         print(self.a, self.b)
#     def S(self):
#         semi_per = (self.a + self.b + self.c) / 2
#         return math.sqrt(semi_per * (semi_per - self.a) * (semi_per - self.b) * (semi_per - self.c))
#     def P(self):
#         return self.a + self.b + self.c
    
# import random

# def get():
#     r = random.randint(0,2)
#     if r == 0:
#         return Circle("Circle", random.randint(2, 5))
#     elif r == 1:
#         return Rectangle("Rectangle", random.randint(2, 5),random.randint(2, 5) )
#     elif r == 2:
#         return Triangle("Triangle", random.randint(2, 5),random.randint(2, 5),random.randint(2, 5))


# figures = []
# for i in range(10):
#     figures.append(get())

# figures.sort(key = lambda figure: figure.S(), reverse=True)
# k = 0

# for figure in figures:
#     if k == 3:
#         break
#     figure.show()
#     print(figure.S())
#     k+=1
# //////////////////////////////////////////////
# Design classes for chess pieces.

# For each type of figure, make a separate class.
# You should implement the class Figure for the base abstract figure
# Implement the step() method, which will check if the move specified by the user is possible.
# The figures on the field are arranged randomly => each figure knows its coordinates.
# The figure cannot go to any field in which it is already standing.
# You can read chess.pdf as a hint in the FILES folder.
# You should use modules for classes. Import modules to main.py and show the results
# ...........................................................................
from classes import *
import copy


# /////////////////////
pole1=copy.deepcopy(pole)
for i in pole1:
    print (i) 

# ///////////////////////////////ввести координаты, сначала строку
k_w.go(1,0)
p_w_1.go(2,0)
r_w_1.go(5,0)

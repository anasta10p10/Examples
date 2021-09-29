# Для созданного класса шахматных фигур сформировать csv файл с информацией о каждой фигуре и ее позиции 
# на шахматной доске
# //////////////////////////////////////////////////////////////
# pole=[['           ' for i in range(8)] for j in range(8)]

# class Figure:
#     def __init__(self, name, color, x, y):
#         self.name = name
#         self.color = color
#         self.x = x
#         self.y = y
#         pole[x][y]= "{:^11}".format(name)

#     def go(self,x1,y1,f):
#         if x1<0 or x1>7 or y1<0 or y1>7:
#             print("can't go beyond the board")
#             return

#         if self.x==x1 and self.y==y1:
#             print('the same place')
#             return

#         if pole[x1][y1]!='           ':
#             print('taken')
#             return
        
#         if f(x1,y1)=='+':
#             pole[x1][y1]="{:^11}".format(self.name)
#             pole[self.x][self.y]='           '
#             self.x = x1
#             self.y = y1
#             print('done')
#             return 
#         else:
#             print('legs are short')
#     def show(self):
#             a=[self.name, self.color, self.x, self.y]
#             return a
# class King(Figure):
#     def __init__(self, name, color, x, y):
#         super().__init__(name, color, x, y)
    
#     def __check(self, x1, y1):
#         if abs(x1-self.x)<=1 and abs(y1-self.y)<=1:
#             return '+'
#         else:
#             return '-'
#     def go(self,x1,y1):
#         super().go(x1, y1, self.__check)
#     def show(self):
#         return super().show()

# class Queen(Figure):
#     def __init__(self, name, color, x, y):
#         super().__init__(name, color, x, y)
    
#     def __check(self, x1, y1):
#         return Bishoop.can_move_to(self, x1, y1) or Rook.can_move_to(self, x1, y1)
       
#     def go(self,x1,y1):
#         super().go(x1, y1, self.__check)
#     def show(self):
#          return  super().show()

# class Bishoop(Figure):
#     def __init__(self, name, color, x, y):
#         super().__init__(name, color, x, y)
    
#     def __check(self, x1, y1):
#         if self.x + self.y == x1 + y1 or self.x - self.y == x1-y1:
#             return '+'
#         else:
#             return '-' 
       
#     def go(self,x1,y1):
#         super().go(x1, y1, self.__check)
#     def show(self):
#         return super().show()

# class Rook(Figure):
#     def __init__(self, name, color, x, y):
#         super().__init__(name, color, x, y)
    
#     def __check(self, x1, y1):
#         if self.x == x1  or self.y == y1:
#             return '+'
#         else:
#             return '-' 
       
#     def go(self,x1,y1):
#         super().go(x1, y1, self.__check)
#     def show(self):
#         return super().show()

# class Knight(Figure):
#     def __init__(self, name, color, x, y):
#         super().__init__(name, color, x, y)
    
#     def __check(self, x1, y1):
#         if ((abs(x1 - self.x) == 1 and abs(y1 - self.y) == 2) or 
#               (abs(x1 - self.x) == 2 and abs(y1 - self.y) == 1)):
#             return '+'
#         else:
#             return '-' 
       
#     def go(self,x1,y1):
#         super().go(x1, y1, self.__check)
#     def show(self):
#         return super().show()

# class Pawn(Figure):
#     def __init__(self, name, color, x, y):
#         super().__init__(name, color, x, y)
    
#     def __check(self, x1, y1):
#         if (((self.color.lower() == 'w' and self.y == y1 and self.x - x1 == -1) or
#             (self.color.lower() == 'b' and self.y == y1 and self.x - x1 == 1))):
#             return '+'
#         else:
#             return '-' 
       
#     def go(self,x1,y1):
#         super().go(x1, y1, self.__check)
#     def show(self):
#         return super().show()
#/////////////////////////////////////////////

# k_w = King("W King", 'w', 0, 3)

# q_w=Queen("W Queen",'w', 0, 4)

# b_w_1 = Bishoop("W Bishoop 1", 'w', 0, 2)
# b_w_2 = Bishoop("W Bishoop 2", 'w', 0, 5)

# kn_w_1 = Knight("W Knight 1", 'w', 0, 1)
# kn_w_2 = Knight("W Knight 2", 'w', 0, 6)

# r_w_1 = Rook("W Rook 1", 'w', 0,0)
# r_w_2 = Rook("W Rook 2", 'w', 0,7)

# p_w_1=Pawn("W Pawn 1", 'w',1,0)
# p_w_2=Pawn("W Pawn 2", 'w',1,1)
# p_w_3=Pawn("W Pawn 3", 'w',1,2)
# p_w_4=Pawn("W Pawn 4", 'w',1,3)
# p_w_5=Pawn("W Pawn 5", 'w',1,4)
# p_w_6=Pawn("W Pawn 6", 'w',1,5)
# p_w_7=Pawn("W Pawn 7", 'w',1,6)
# p_w_8=Pawn("W Pawn 8", 'w',1,7)
# # -----------------------------

# k_b = King("B King", 'b', 7, 3)

# q_b=Queen("B Queen",'b', 7, 4)

# b_b_1 = Bishoop("B Bishoop 1", 'b', 7, 2)
# b_b_2 = Bishoop("B Bishoop 2", 'b', 7, 5)

# kn_b_1 = Knight("B Knight 1", 'b', 7, 1)
# kn_b_2 = Knight("B Knight 2", 'b', 7, 6)

# r_b_1 = Rook("B Rook 1", 'b', 7,0)
# r_b_2 = Rook("B Rook 2", 'b', 7,7)

# p_b_1=Pawn("B Pawn 1", 'b',6,0)
# p_b_2=Pawn("B Pawn 2", 'b',6,1)
# p_b_3=Pawn("B Pawn 3", 'b',6,2)
# p_b_4=Pawn("B Pawn 4", 'b',6,3)
# p_b_5=Pawn("B Pawn 5", 'b',6,4)
# p_b_6=Pawn("B Pawn 6", 'b',6,5)
# p_b_7=Pawn("B Pawn 7", 'b',6,6)
# p_b_8=Pawn("B Pawn 8", 'b',6,7)

# //////////////////////////////////

# import csv
# heading=["Figure","Color","X","Y"]
# data_for_csv=[k_w, q_w, b_w_1, b_w_2, kn_w_1, kn_w_2, r_w_1, r_w_2, p_w_1, p_w_2, p_w_3, p_w_4, p_w_5, p_w_6, p_w_7, p_w_8, k_b, q_b, b_b_1, b_b_2, kn_b_1, kn_b_2, r_b_1, r_b_2, p_b_1, p_b_2, p_b_3, p_b_4, p_b_5, p_b_6, p_b_7, p_b_8]

# print(k_w.show())

# with open('data/hw12_file.csv', 'w', newline="") as csv_file:
#     writer = csv.writer(csv_file)
#     writer.writerow(heading)
#     for i in data_for_csv:
#         writer.writerow(i.show())
# ///////////////////////////////////////
# Find the sum of numbers on http://python-data.dr-chuck.net/regex_sum_201873.txt.

# import requests
# import re

# url="http://python-data.dr-chuck.net/regex_sum_201873.txt"
# response = requests.get(url) #возвращает ответ от сайта
# print(response.text)
# text=response.text.split()
# print(text)
# numbers=[]
# for word in text:
#     if re.search('\d+', word):
#         numbers.append(int(re.search('\d+', word).group()))
#     else:
#         continue
# print(sum(map(int, re.findall('\d+', response.text))))
# /////////////////////////////////////////////////////////////////
# Find the sum of numbers inside count on http://python-data.dr-chuck.net/comments_200531.xml.
# .....................
# import requests
# import xml.etree.ElementTree as xml

# url="http://python-data.dr-chuck.net/comments_200531.xml"
# response = requests.get(url).text #возвращает ответ от сайта
# tree = xml.fromstring(response)
# mas=[]
# for count in tree.iter('count'):
#     mas.append(int(count.text))
# print(sum(mas))

# ////////////////////////////////////////////////////////////////////

# Дан текст
# Выполнять все задания для текста между *** START OF THE PROJECT GUTENBERG EBOOK THE IDIOT ***
# (в начале книги) и *** END OF THE PROJECT GUTENBERG EBOOK THE IDIOT *** (в конце книги)
# Заменить все символы ";" на "."
# Найти кол-во вхождений артикля the в тексте в любом регистре
# Найдите, сколько раз кто-либо был процитирован (текст в кавычках).
import requests
import re
import chardet

from requests.models import Response

url="https://www.gutenberg.org/files/2638/2638-0.txt"
response = requests.get(url)
response.encoding=chardet.detect(response.content)
response=response.text
# print(response)
book=re.split('\*\*\* END OF THE PROJECT GUTENBERG EBOOK THE IDIOT \*\*\*', re.split('\*\*\* START OF THE PROJECT GUTENBERG EBOOK THE IDIOT \*\*\*', response)[1])[0]

book=book.replace(';','.')
print(book[-1:-100:-1])
# res= re.findall('\W+the\W+/i',book)
res= re.findall(r'\W+the\W+',book,re.IGNORECASE)
print(len(res))

cov=re.findall(r'\“',book)
cov1=re.findall(r'\”',book)
print(len(cov),len(cov1))
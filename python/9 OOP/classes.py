pole=[['           ' for i in range(8)] for j in range(8)]

class Figure:
    def __init__(self, name, color, x, y):
        self.name = name
        self.color = color
        self.x = x
        self.y = y
        pole[x][y]= "{:^11}".format(name)

    def go(self,x1,y1,f):
        if x1<0 or x1>7 or y1<0 or y1>7:
            print("can't go beyond the board")
            return

        if self.x==x1 and self.y==y1:
            print('the same place')
            return

        if pole[x1][y1]!='           ':
            print('taken')
            return
        
        if f(x1,y1)=='+':
            pole[x1][y1]="{:^11}".format(self.name)
            pole[self.x][self.y]='           '
            self.x = x1
            self.y = y1
            print('done')
            return 
        else:
            print('legs are short')

class King(Figure):
    def __init__(self, name, color, x, y):
        super().__init__(name, color, x, y)
    
    def __check(self, x1, y1):
        if abs(x1-self.x)<=1 and abs(y1-self.y)<=1:
            return '+'
        else:
            return '-'
    def go(self,x1,y1):
        super().go(x1, y1, self.__check)

class Queen(Figure):
    def __init__(self, name, color, x, y):
        super().__init__(name, color, x, y)
    
    def __check(self, x1, y1):
        return Bishoop.can_move_to(self, x1, y1) or Rook.can_move_to(self, x1, y1)
       
    def go(self,x1,y1):
        super().go(x1, y1, self.__check)

class Bishoop(Figure):
    def __init__(self, name, color, x, y):
        super().__init__(name, color, x, y)
    
    def __check(self, x1, y1):
        if self.x + self.y == x1 + y1 or self.x - self.y == x1-y1:
            return '+'
        else:
            return '-' 
       
    def go(self,x1,y1):
        super().go(x1, y1, self.__check)

class Rook(Figure):
    def __init__(self, name, color, x, y):
        super().__init__(name, color, x, y)
    
    def __check(self, x1, y1):
        if self.x == x1  or self.y == y1:
            return '+'
        else:
            return '-' 
       
    def go(self,x1,y1):
        super().go(x1, y1, self.__check)

class Knight(Figure):
    def __init__(self, name, color, x, y):
        super().__init__(name, color, x, y)
    
    def __check(self, x1, y1):
        if ((abs(x1 - self.x) == 1 and abs(y1 - self.y) == 2) or 
              (abs(x1 - self.x) == 2 and abs(y1 - self.y) == 1)):
            return '+'
        else:
            return '-' 
       
    def go(self,x1,y1):
        super().go(x1, y1, self.__check)

class Pawn(Figure):
    def __init__(self, name, color, x, y):
        super().__init__(name, color, x, y)
    
    def __check(self, x1, y1):
        if (((self.color.lower() == 'w' and self.y == y1 and self.x - x1 == -1) or
            (self.color.lower() == 'b' and self.y == y1 and self.x - x1 == 1))):
            return '+'
        else:
            return '-' 
       
    def go(self,x1,y1):
        super().go(x1, y1, self.__check)
#/////////////////////////////////////////////
k_w = King("W King", 'w', 0, 3)

q_w=Queen("W Queen",'w', 0, 4)

b_w_1 = Bishoop("W Bishoop 1", 'w', 0, 2)
b_w_2 = Bishoop("W Bishoop 2", 'w', 0, 5)

kn_w_1 = Knight("W Knight 1", 'w', 0, 1)
kn_w_2 = Knight("W Knight 2", 'w', 0, 6)

r_w_1 = Rook("W Rook 1", 'w', 0,0)
r_w_2 = Rook("W Rook 2", 'w', 0,7)

p_w_1=Pawn("W Pawn 1", 'w',1,0)
p_w_2=Pawn("W Pawn 2", 'w',1,1)
p_w_3=Pawn("W Pawn 3", 'w',1,2)
p_w_4=Pawn("W Pawn 4", 'w',1,3)
p_w_5=Pawn("W Pawn 5", 'w',1,4)
p_w_6=Pawn("W Pawn 6", 'w',1,5)
p_w_7=Pawn("W Pawn 7", 'w',1,6)
p_w_8=Pawn("W Pawn 8", 'w',1,7)
# -----------------------------

k_b = King("B King", 'b', 7, 3)

q_b=Queen("B Queen",'b', 7, 4)

b_b_1 = Bishoop("B Bishoop 1", 'b', 7, 2)
b_b_2 = Bishoop("B Bishoop 2", 'b', 7, 5)

kn_b_1 = Knight("B Knight 1", 'b', 7, 1)
kn_b_2 = Knight("B Knight 2", 'b', 7, 6)

r_b_1 = Rook("B Rook 1", 'b', 7,0)
r_b_2 = Rook("B Rook 2", 'b', 7,7)

p_b_1=Pawn("B Pawn 1", 'b',6,0)
p_b_2=Pawn("B Pawn 2", 'b',6,1)
p_b_3=Pawn("B Pawn 3", 'b',6,2)
p_b_4=Pawn("B Pawn 4", 'b',6,3)
p_b_5=Pawn("B Pawn 5", 'b',6,4)
p_b_6=Pawn("B Pawn 6", 'b',6,5)
p_b_7=Pawn("B Pawn 7", 'b',6,6)
p_b_8=Pawn("B Pawn 8", 'b',6,7)
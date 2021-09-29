# Создать пакет, содержащий 2 модуля.
# В первом модуле будут лежать функция, принимающая на вход число и возвращающая факториал этого числа, и функция,
# принимающее число в градусах и переводящее его в радианы.
# Второй модуль будет содержать функцию, принимающую на вход сторону квадрата и возвращающая его площадь.
# В главном файле файле продемонстрировать использование этих модулей.
# ..................................................
# from package import mod1, mod2
# print(mod1.fact(3))
# print(mod1.rad(30))
# print(mod2.s(5))
# //////////////////////////////////////////////
# Создать, используя conda, окружение. Установить произвольные пакеты. Создать файл env.yml с уставновленными пакетами. 
# (При проблемах с conda можно использовать venv, например)
# Написать документацию к функции для игры Быки и коровы
# ////////////////////////////////////////////////
import sys
players={'Игрок 1':input('Игрок 1 - Тайное число: Введите 4-значное число без повторения цифр'), 
'Игрок 2': input('Игрок 2 - Тайное число: Введите 4-значное число без повторения цифр')}
t=True
while True:
    for i in players:
        if len(players[i])==4 and len(set(players[i]))==4 and players[i].isdigit()==True:
            t=False
            pass
        else:
            players[i]=input(f'{i} : Вы ввели не подходящее число.Введите 4-значное число без повторения цифр')  
    if not t:
        break
# Checks if the numbers are appropriate.
x=0
pos_var={'Игрок 1':0,'Игрок 2':0}
def prov(p,n,pl): #где p-чей ход, п-число на проверку, pl - проверка для какого игрока
    """Compares the entered number with the entended one. Prints result in 'b' and 'k'.
    
    If the digit corresponds the digit of the entended number, 'b' increases by 1.
    If the digit in the entended number, but in another place, 'k' increases by 1
    
    Args:
        p (str): The player to go.
        n (str): The number to check/
        pl (str): The number to compare.

    Returns:
        str: Prints result in 'b' and 'k'.
    """
    b=0
    k=0
    for i in range(len(n)):
        if pl[i]==n[i]:
            b+=1
        elif n[i] in pl:
            k+=1
    if b==4:
        x="Точное попадание!"
        pos_var[p]=x
        print(x)
        return x
    x= f'Результат: {k} «коров(ы)» и {b} «бык(ов)»'
    print(x)
    pos_var[p]=x
t = True
while True:
    if  "Точное попадание!" not in pos_var.values():
        prov('Игрок 1',input("Введите 4-значное число без повторения цифр"),players['Игрок 2'])
        prov('Игрок 2',input("Введите 4-значное число без повторения цифр"),players['Игрок 1'])
    elif pos_var['Игрок 1']=="Точное попадание!" and pos_var['Игрок 2']=="Точное попадание!":
        print("Ничья")
        break
    else:
        for i in pos_var:
            if pos_var[i]=="Точное попадание!":
                print(f'{players[i]}, Вы победили!!!')
                t=False
                break
         
        if not t:
            break


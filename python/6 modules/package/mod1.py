# В первом модуле будут лежать функция, принимающая на вход число и возвращающая факториал этого числа, 
# и функция, принимающее число в градусах и переводящее его в радианы.
def fact(number):
    res=1
    for i in range(1,number+1):
        res*=i
    return res

def rad(grad):
    res=grad*0.0174533
    return res

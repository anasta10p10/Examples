import numpy as np
scores = np.array([[20, 40, 56, 80, 0, 5, 25, 27, 74, 1],
         [0, 98, 67, 100, 8, 56, 34, 82, 100, 7],
         [78, 54, 23, 79, 100, 0, 0, 42, 95, 83],
         [51, 50, 47, 23, 100, 94, 25, 48, 38, 77],
         [90, 87, 41, 89, 52, 0, 5, 17, 28, 99],
         [32, 18, 21, 18, 29, 31, 48, 62, 76, 22],
         [6, 0, 65, 78, 43, 22, 38, 88, 94, 100],
         [77, 28, 39, 41, 0, 81, 45, 54, 98, 12],
         [66, 0, 88, 0, 44, 0, 55, 100, 12, 11],
         [17, 70, 86, 96, 56, 23, 32, 49, 70, 80],
         [20, 24, 76, 50, 29, 40, 3, 2, 5, 11],
         [33, 63, 28, 40, 51, 100, 98, 87, 22, 30],
         [16, 54, 78, 12, 25, 35, 10, 19, 67, 0],
         [100, 88, 24, 33, 47, 56, 62, 34, 77, 53],
         [50, 89, 70, 72, 56, 29, 15, 20, 0, 0]])

# Посчитать, сколько слушателей получили 0 за вступительный экзамен.
print(f' 0 получили {(scores==0).sum()} слушателей')
# Посчитать, сколько слушателей получили балл выше 50.
print(f'больше 50 получили {(scores>50).sum()} слушателей')
# Посчитать, сколько человек получили балл не ниже 50, но не выше 70.
print(f'не меньше 50, но не выше 70 получили {((50<=scores) & (scores<=70)).sum()} слушателей')
# Определить, в какой группе средний балл за вступительный экзамен выше.
print(f'средний балл за вступительный экзамен больше в {(scores.mean(axis=1)).argmax()} группе')
# Сохранить баллы слушателей выше 0 в массив `nonzero`. 
nonzero = scores[scores >0 ]
print(nonzero)
# Используя массив `nonzero`, определить минимальный балл за вступительный балл по всем группам.
print(nonzero.min())
# Выбрать из массива `nonzero` только те значения, которые соответствуют продвинутому уровню знания языка – баллу за экзамен выше 80.
#  Сохранить полученный результат в массив `advanced`. 
advanced = nonzero[nonzero > 80]
print(advanced)
# Определить размерность массива `advanced`.
print(advanced.ndim)
# Определить форму массива `advanced`.
print(advanced.shape)
# Определить общее число элементов в массиве `advanced`.
print(advanced.size)
# На основе исходного массива `scores` создать булев массив `sto`, где `True` соответствует баллам за экзамен, равным 100, 
# а `False` – всем остальным баллам.
sto = (scores==100)
print(sto)
# На основе исходного массива `scores` вывести на экран оценки слушателей первых семи групп 
# (включительно, должны быть 7 списков оценок).
print(scores[:7])

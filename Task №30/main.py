"""
Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент,
разность и количество элементов нужно ввести с клавиатуры.
Формула для получения n-го члена прогрессии: A_n = A_1 + (n-1) * d.
Каждое число вводится с новой строки.

"""

A_1 = int(input("Введите первый член арифметической прогрессии: "))
d = int(input("Введите разность арифметической прогрессии: "))
n = int(input("Введите число членов арифметической прогрессии: ")) # число итераций i == числу членов прогрессии n!! Это условие для решения задачи
for i in range(n):
    A_n= A_1 + i * d
    print(A_n)


"""
Задача 32: Определить индексы элементов массива (списка), 
значения которых принадлежат заданному диапазону
 (т.е. не меньше заданного минимума и не больше заданного максимума)
"""


from random import randint

def Bubble_sorting_list(rand_list):
    for i in rand_list(len(rand_list)-1):
        for j in rand_list(len(rand_list)-i-1):
            if rand_list[j] > rand_list[j + 1]:
                rand_list[j], rand_list[j + 1] = rand_list[j + 1], rand_list[j]
                print(rand_list, 'end=')


#
# lower=int(input("Введите нижнюю границу рандомайзера: "))
# upper=int(input("Введите верхнюю границу рандомайзера: "))
# rand_list=[]
#
# n=int(input("Введите длину списка из случайных чисел: "))
#
# for _ in range(n):
#     rand_list.append(randint(lower,upper))
#     print(rand_list)
#
# Bubble_sorting_list(rand_list)
"""
Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
Пользователь вводит 2 числа. n — кол-во элементов первого множества.
m — кол-во элементов второго множества.
 Затем пользователь вводит сами элементы множеств.
"""


from random import randint

n=(int(input("Введите число n элементов: ")))
m=(int(input("Введите число m элементов: ")))


num_list_1=[]
for i in range(n):
    num_n = int(input("Введите num_n "))
    num_list_1.append(num_n)
print(num_list_1)

num_list_2 = []
for i in range(m):
    num_m = int(input("Введите num_m "))
    num_list_2.append(num_m)
print(num_list_2)


num_list3 = num_list_1+num_list_2

print(num_list3)




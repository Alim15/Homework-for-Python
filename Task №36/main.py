# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает
# в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы
# (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция,
# у которой ровно два аргумента, как, например, у операции умножения.

def print_operation_table(operation, num_rows, num_cols):
    for row in range(1, num_rows+1):
        for cols in range(1, num_cols+1):
            result=operation(row, cols)
            print(result, end='t')


num_rows=int(input("Введите число строк: "))
num_cols=int(input("Введите число столбцов: "))


# Напишите следующие функции:
# 1 Нахождение корней квадратного уравнения
# 2 Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
# 3 Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой тройкой чисел из csv файла.
# 4 Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.

import csv
import json
import math
import os.path
from random import randint
from typing import Callable

# Генерация csv файла со случайными числами        
def coeffs_csv():
    with open('coefficients.csv', 'w', newline='', encoding='UTF-8') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC)
        for _ in range(randint(100, 1000)):
            writer.writerow([randint(-100, 100), randint(-100, 100), randint(-100, 100)])

# Декоратор нахождения корней
def deco_solve_for_csv(func):
    solutions_dict = {}
    
    def wrapper(*args, **kwargs):
        with open('coefficients.csv', 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=',')
            for row in reader:
                result = func(int(row[0]), int(row[1]), int(row[2]))
                rows = f'a = {row[0]}, b = {row[1]}, c = {row[2]}'
                solutions_dict[str(rows)] = str(result)
        return solutions_dict
    return wrapper

# Декоратор, сохраняющий результаты в json файл
def deco_result_to_json(func):
    def wrapper(*args, **kwargs):
        with open('solutions.json', 'w', encoding='utf=8') as file:
            json.dump(func('coefficients.csv'), file, indent=2, separators=(',', ':'), ensure_ascii=False)
    return wrapper

# Нахождение корней квадратного уравнения
@deco_result_to_json
@deco_solve_for_csv
def roots_of_quadratic_equation(*args) -> tuple | float | None:
    a, b, c = args
    if a == 0:
        return "Не является квадратным уравнением"
    else:        
        d = b ** 2 - 4 * a * c
        if d > 0:
            root_1 = (-b + math.sqrt(d)) / (2 * a)
            root_2 = (-b - math.sqrt(d)) / (2 * a)
            return f"Корни уравнения: x1 = {round(root_1, 2)}, x2 = {round(root_2, 2)}"
        elif d == 0:
            root = -b / (2 * a)
            return f"Корень уравнения: x = {round(root, 2)}"
        else:
            return "Корней нет"

coeffs_csv()
roots_of_quadratic_equation()
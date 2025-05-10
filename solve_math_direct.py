#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
from math import pi, sqrt


# Определяем функции
def compute_arc_length(radius, angle_in_degrees):
    """Вычисляет длину дуги по радиусу и углу в градусах"""
    return (angle_in_degrees / 360) * 2 * pi * radius


def compute_triangle_area(a, b, c):
    """Вычисляет площадь треугольника по длинам его сторон"""
    s = (a + b + c) / 2
    return sqrt(s * (s - a) * (s - b) * (s - c))


def convert_meters_to_cm(num):
    """Переводит метры в сантиметры"""
    return num * 100


def convert_cubic_cm_to_liters(num):
    """Переводит кубические сантиметры в литры"""
    return num / 1000


def compute_rectangle_perimeter(a, b):
    """Вычисляет периметр прямоугольника"""
    return 2 * (a + b)


def compute_circle_area(radius):
    """Вычисляет площадь круга"""
    return pi * radius**2


def compute_cylinder_volume(radius, height):
    """Вычисляет объем цилиндра"""
    return pi * radius**2 * height


def compute_cube_volume(a):
    """Вычисляет объем куба"""
    return a**3


def convert_binary_to_decimal(binary_number):
    """Переводит число из двоичной системы счисления в десятичную систему счисления"""
    return int(binary_number, 2)


def convert_decimal_to_binary(decimal_number):
    """Переводит число из десятичной системы счисления в двоичную систему счисления"""
    return bin(decimal_number)[2:]  # [2:] отрезает префикс '0b'


def get_count_ones(number):
    """Находит количество единиц в двоичном представлении числа"""
    # Если передано десятичное число, сначала переводим его в двоичную систему
    if isinstance(number, int):
        binary = bin(number)[2:]
    else:
        # Если передана строка, проверяем, что это двоичное число
        try:
            int(number, 2)
            binary = number
        except ValueError:
            # Если это не двоичное число, считаем, что это десятичное и переводим
            binary = bin(int(number))[2:]

    return binary.count("1")


def main():
    # Загружаем данные
    df = pd.read_csv(
        "https://stepik.org/media/attachments/lesson/1110884/custom_math_tools.csv"
    )

    # Решаем задачи
    answers = []

    # Задача 1: Периметр прямоугольника в см
    perimeter_m = compute_rectangle_perimeter(1.5, 2)  # в метрах
    perimeter_cm = convert_meters_to_cm(perimeter_m)  # перевод в см
    answers.append(perimeter_cm)  # 700

    # Задача 2: Сумма площадей кругов
    area1 = compute_circle_area(5)  # площадь первого круга
    area2 = compute_circle_area(3)  # площадь второго круга
    total_area = area1 + area2
    answers.append(total_area)  # примерно 106.81

    # Задача 3: Сумма единиц в двоичных представлениях
    bin_20 = convert_decimal_to_binary(20)  # 10100
    bin_32 = convert_decimal_to_binary(32)  # 100000
    ones_count = get_count_ones(bin_20) + get_count_ones(bin_32)
    answers.append(ones_count)  # 2 + 1 = 3

    # Задача 4: Сумма чисел из двоичной системы
    num1 = convert_binary_to_decimal("1101011010")  # 858
    num2 = convert_binary_to_decimal("101011")  # 43
    total_sum = num1 + num2
    answers.append(total_sum)  # 901

    # Задача 5: Объем цилиндра в литрах
    volume_cm3 = compute_cylinder_volume(10, 30)  # в куб. см
    volume_liters = convert_cubic_cm_to_liters(volume_cm3)
    answers.append(volume_liters)  # примерно 9.42

    # Задача 6: Длина дуги в сантиметрах
    arc_length_m = compute_arc_length(20, 60)  # в метрах
    arc_length_cm = convert_meters_to_cm(arc_length_m)
    answers.append(arc_length_cm)  # примерно 2094.4

    # Задача 7: Количество единиц в двоичном представлении числа
    ones_count = get_count_ones("1524")
    answers.append(ones_count)  # 7

    # Задача 8: Объем куба в двоичной системе
    cube_volume = compute_cube_volume(5)  # 125
    cube_volume_bin = convert_decimal_to_binary(int(cube_volume))
    answers.append(cube_volume_bin)  # "1111101" числовое значение "125"

    # Задача 9: Площадь треугольника
    # Переводим сторону из двоичной системы
    side3_decimal = convert_binary_to_decimal("110010")  # 50

    triangle_area = compute_triangle_area(30, 40, side3_decimal)
    answers.append(triangle_area)  # примерно 600

    # Задача 10: Сумма объемов цилиндров в литрах
    cylinder1_volume = compute_cylinder_volume(8, 20)  # в куб. см
    cylinder2_volume = compute_cylinder_volume(12, 25)  # в куб. см

    total_volume_cm3 = cylinder1_volume + cylinder2_volume
    total_volume_liters = convert_cubic_cm_to_liters(total_volume_cm3)
    answers.append(total_volume_liters)  # примерно 13.7

    # Создаем DataFrame для записи результатов
    result_df = pd.DataFrame({"task": df["task"], "answer": answers})

    # Сохраняем результаты
    result_df.to_csv("math_solutions.csv", index=False)
    print("Готово! Ответы сохранены в файл math_solutions.csv")

    # Выводим результаты
    print("\nРезультаты:")
    for i, (task, answer) in enumerate(zip(df["task"], answers)):
        print(f"{i+1}. {task}")
        print(f"   Ответ: {answer}")
        print()


if __name__ == "__main__":
    main()

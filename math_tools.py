from math import pi, sqrt
from langchain.agents import tool


@tool
def compute_arc_length(radius, angle_in_degrees):
    """Вычисляет длину дуги по радиусу и углу в градусах"""
    return (angle_in_degrees / 360) * 2 * pi * radius


@tool
def compute_triangle_area(a, b, c):
    """Вычисляет площадь треугольника по длинам его сторон"""
    s = (a + b + c) / 2
    return sqrt(s * (s - a) * (s - b) * (s - c))


# Реализуем остальные функции
@tool
def add_numbers(num1, num2):
    """Складывает два числа"""
    return num1 + num2


@tool
def convert_meters_to_cm(num):
    """Переводит метры в сантиметры"""
    return num * 100


@tool
def convert_cubic_cm_to_liters(num):
    """Переводит кубические сантиметры в литры"""
    return num / 1000


@tool
def compute_rectangle_perimeter(a, b):
    """Вычисляет периметр прямоугольника"""
    return 2 * (a + b)


@tool
def compute_circle_area(radius):
    """Вычисляет площадь круга"""
    return pi * radius**2


@tool
def compute_cylinder_volume(radius, height):
    """Вычисляет объем цилиндра"""
    return pi * radius**2 * height


@tool
def compute_cube_volume(a):
    """Вычисляет объем куба"""
    return a**3


@tool
def convert_binary_to_decimal(binary_number: str):
    """Переводит число из двоичной системы счисления в десятичную систему счисления"""
    return int(binary_number, 2)


@tool
def convert_decimal_to_binary(decimal_number):
    """Переводит число из десятичной системы счисления в двоичную систему счисления"""
    return bin(decimal_number)[2:]  # [2:] отрезает префикс '0b'


@tool
def get_count_ones(number: str):
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


# Поместим все написанные функции в tools
tools = [
    compute_arc_length,
    compute_triangle_area,
    add_numbers,
    convert_meters_to_cm,
    convert_cubic_cm_to_liters,
    compute_rectangle_perimeter,
    compute_circle_area,
    compute_cylinder_volume,
    compute_cube_volume,
    convert_binary_to_decimal,
    convert_decimal_to_binary,
    get_count_ones,
]

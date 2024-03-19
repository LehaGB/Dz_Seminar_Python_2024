"""
Рекурсивная сумма
Напишите рекурсивную функцию sum(a, b), 
возвращающую сумму двух целых неотрицательных чисел. 
Из всех арифметических операций допускаются только +1 и -1. 
Также нельзя использовать циклы.
"""

# def sum_number(a: int, b: int) -> int:
#     while b > 0:
#         b -= 1
#         a += 1
#     return a


def sum(a: int, b: int) -> int:
    """Принимает два числа и возвращает
    сумму двух чисел с помощью рекурсии.

    Args:
        num1 (int): положительное число
        num2 (int): положительное число

    Returns:
        int: сумма двух чисел
    """
    count = 0

    if a == 0 or b == 0:
        return a + b
    if count < b:
        count += 1
        return sum(a + 1, b - 1)


print(sum(3, 9))

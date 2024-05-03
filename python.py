"""
Задана рекуррентная функция. Область определения функции – натуральные числа. 
Написать программу сравнительного вычисления данной функции рекурсивно и итерационно. 
Определить границы применимости рекурсивного и итерационного подхода. 
Результаты сравнительного исследования времени вычисления представить 
в табличной и графической форме в виде отчета по лабораторной работе.

Вариант 26. F(1) = 1; G(1) = 1; F(n) =(-1)**n * (F(n–1) – G(n–1)), G(n) = F(n–1) + 2*G(n–1) /(2n)!, при n >=2
"""

import time

cache_recursive_F = {}
cache_recursive_G = {}

factorials = {0: 1, 1: 1}

def factorial(n):
    if n not in factorials:
        result = 1
        for i in range(2, n + 1):
            result *= i
            factorials[i] = result
    return factorials[n]

def recursive_F(n):
    if n == 1:
        return 1
    if n not in cache_recursive_F:
        if n % 2 == 0:
            cache_recursive_F[n] = (-1) ** 2 * (recursive_F(n - 1) - recursive_G(n - 1))
        else:
            cache_recursive_F[n] = (-1) ** 1 * (recursive_F(n - 1) - recursive_G(n - 1))
    return cache_recursive_F[n]

def recursive_G(n):
    if n == 1:
        return 1
    if n not in cache_recursive_G:
        cache_recursive_G[n] = recursive_F(n - 1) + 2 * recursive_G(n - 1) / factorial(2 * n)
    return cache_recursive_G[n]

def iterative_F(n):
    f, g = 1, 1
    for i in range(2, n + 1):
        f, g = (-1) ** i * (f - g), f + 2 * g / factorial(2 * i)
    return f

def iterative_G(n):
    f, g = 1, 1
    for i in range(2, n + 1):
        f, g = (-1) ** i * (f - g), f + 2 * g / factorial(2 * i)
    return g

n = int(input('Введите натуральное число: '))
while not (2 <= n):
    print('Число не является допустимым значением.')
    n = int(input('Повторите ввод:'))

start_time = time.time()
recursive_f_result = recursive_F(n)
recursive_g_result = recursive_G(n)
recursive_time = time.time() - start_time

start_time = time.time()
iterative_f_result = iterative_F(n)
iterative_g_result = iterative_G(n)
iterative_time = time.time() - start_time

print("Recursive F({}) = {}, time: {:.6f} seconds".format(n, recursive_f_result, recursive_time))
print("Recursive G({}) = {}, time: {:.6f} seconds".format(n, recursive_g_result, recursive_time))
print("Iterative F({}) = {}, time: {:.6f} seconds".format(n, iterative_f_result, iterative_time))
print("Iterative G({}) = {}, time: {:.6f} seconds".format(n, iterative_g_result, iterative_time))

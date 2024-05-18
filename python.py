"""
Задана рекуррентная функция. Область определения функции – натуральные числа. 
Написать программу сравнительного вычисления данной функции рекурсивно и итерационно. 
Определить границы применимости рекурсивного и итерационного подхода. 
Результаты сравнительного исследования времени вычисления представить 
в табличной и графической форме в виде отчета по лабораторной работе.

Вариант 26. F(1) = 1; G(1) = 1; F(n) =(-1)**n * (F(n–1) – G(n–1)), G(n) = F(n–1) + 2*G(n–1) /(2n)!, при n >=2
"""
import time

class SingleItemCache:
    def __init__(self):
        self.item = None

    def add(self, item):
        self.item = item

    def get(self):
        return self.item

# Создаем экземпляр кэша
cache = SingleItemCache()
cache_F = SingleItemCache()
cache_G = SingleItemCache()
factorials = SingleItemCache()

def memoize(func):
    cached_results = {}
    def wrapper(n, cache):
        if n not in cached_results:
            cached_results[n] = func(n, cache)
        return cached_results[n]
    return wrapper

@memoize
def factorial(n, cache):
    if n == 0:
        return 1
    if n != cache.get():
        result = 1
        for i in range(1, n + 1):
            result *= i
        cache.add(n)
        cache.add(result)
    return cache.get()

@memoize
def recursive_F(n, cache):
    if n == 1:
        return 1
    if n != cache.get():
        if n % 2 == 0:
            cache.add((-1) ** 2 * (recursive_F(n - 1, cache) - recursive_G(n - 1, cache)))
        else:
            cache.add((-1) ** 1 * (recursive_F(n - 1, cache) - recursive_G(n - 1, cache)))
        return cache.get()

@memoize
def recursive_G(n, cache):
    if n == 1:
        return 1
    if n != cache.get():
        cache.add(recursive_F(n - 1, cache) + 2 * recursive_G(n - 1, cache) / factorial(2 * n, factorials))
    return cache.get()

def iterative_F(n):
    f, g = 1, 1
    for i in range(2, n + 1):
        if n % 2 == 0:
            f, g = (-1) ** 2 * (f - g), f + 2 * g / factorial(2 * i, factorials)
        else:
            f, g = (-1) ** 1 * (f - g), f + 2 * g / factorial(2 * i, factorials)
    return f

def iterative_G(n):
    f, g = 1, 1
    for i in range(2, n + 1):
        if n % 2 == 0:
            f, g = (-1) ** 2 * (f - g), f + 2 * g / factorial(2 * i, factorials)
        else:
            f, g = (-1) ** 1 * (f - g), f + 2 * g / factorial(2 * i, factorials)
    return g

n = int(input('Введите натуральное число: '))
while not (2 <= n):
    print('Число не является допустимым значением.')
    n = int(input('Повторите ввод:'))

start_time = time.time()
recursive_f_result = recursive_F(n, cache_F)
recursive_g_result = recursive_G(n, cache_G)
recursive_time = time.time() - start_time

start_time = time.time()
iterative_f_result = iterative_F(n)
iterative_g_result = iterative_G(n)
iterative_time = time.time() - start_time

print("Recursive F({}) = {}, time: {:.6f} seconds".format(n, recursive_f_result, recursive_time))
print("Recursive G({}) = {}, time: {:.6f} seconds".format(n, recursive_g_result, recursive_time))
print("Iterative F({}) = {}, time: {:.6f} seconds".format(n, iterative_f_result, iterative_time))
print("Iterative G({}) = {}, time: {:.6f} seconds".format(n, iterative_g_result, iterative_time))

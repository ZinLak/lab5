"""
Задана рекуррентная функция. Область определения функции – натуральные числа. 
Написать программу сравнительного вычисления данной функции рекурсивно и итерационно. 
Определить границы применимости рекурсивного и итерационного подхода. 
Результаты сравнительного исследования времени вычисления представить 
в табличной и графической форме в виде отчета по лабораторной работе.

Вариант 26. F(1) = 1; G(1) = 1; F(n) =(-1)**n * (F(n–1) – G(n–1)), G(n) = F(n–1) + 2*G(n–1) /(2n)!, при n >=2
"""

import time
import matplotlib.pyplot as plt

factorials = {'key': 0, 'item': 1}
cache_F = {}
cache_G = {}
cache_alternationSign = {'sign': None}

timer=[]
timer_rec=[]

def factorial(n):
    if n != factorials['key']:
        if factorials['item'] is None or (n != factorials['key'] + 1 and n != factorials['key'] - 1):
            result = 1
            for i in range(1, n + 1):
                result *= i
            factorials['key'], factorials['item'] = n, result
            return factorials['item']
        else:
            if n > factorials['key']:
                factorials['key'] += 1
                factorials['item'] *= factorials['key']
            elif n < factorials['key']:
                factorials['item'] //= factorials['key']
                factorials['key'] -= 1
            return factorials['item']
    else:
        return factorials['item']

def recursive_F(n):
    if n == 1:
        return 1
    if n not in cache_F:
        cache_alternationSign['sign'] = -1 if n % 2 == 1 else 1
        cache_F.clear()
        cache_F[n] = cache_alternationSign['sign'] * (recursive_F(n - 1) - recursive_G(n - 1))
    return cache_F[n]

def recursive_G(n):
    if n == 1:
        return 1
    if n not in cache_G:
        cache_G.clear()
        cache_G[n] = recursive_F(n - 1) + 2 * recursive_G(n - 1) / factorial(2 * n)
    return cache_G[n]

def iterative_F(n):
    if n == 1:
        return 1
    f, g = 1, 1
    for i in range(2, n + 1):
        sign = -1 if i % 2 == 1 else 1
        f, g = sign * (f - g), f + 2 * g / factorial(2 * i)
    return f

def iterative_G(n):
    if n == 1:
        return 1
    f, g = 1, 1
    for i in range(2, n + 1):
        sign = -1 if i % 2 == 1 else 1
        f, g = sign * (f - g), f + 2 * g / factorial(2 * i)
    return g

n = int(input('Введите натуральное число: '))
while n < 2:
    n = int(input('Введите натуральное число (min 2): '))

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

graf = list(range(1, n+1))

for i in graf:
    start = time.time()
    result = iterative_F(i)
    end = time.time()
    timer.append(end-start)
    start_rec = time.time()
    res = recursive_F(i)
    end_rec = time.time()
    timer_rec.append(end_rec-start_rec)

plt.plot(graf, timer, label='Итерационная функция.')
plt.plot(graf, timer_rec, label='Рекусионная функция.')
plt.legend(loc=2)

plt.xlabel('Значение n')
plt.ylabel('Время выполнения (c)')
plt.show()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Написать функцию, вычисляющую среднее
гармоническое своих аргументов
"""


def G(*args):
    if args:
        # list comprehension (генератр списков)
        values = [int(arg) for arg in args]

        n = len(values)
        i, summ = 0, 0
        for i, value in enumerate(values, 0):
            summ += 1 / value
        garm = n / summ
        return garm
    else:
        return None


if __name__ == "__main__":
    ar = input('Введите аргументы:\n').split()
    print('Среднее гармоническое: ', G(*ar))

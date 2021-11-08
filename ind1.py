#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Написать функцию, вычисляющую сумму аргументов,
расположенных после первого положительного аргумента
"""


def G(*args):
    if args:
        summ = 0
        for i, value in enumerate(args):
            if float(value) > 0:
                for value2 in args[i + 1:]:
                    summ += float(value2)
                return summ
    else:
        return None


if __name__ == "__main__":
    print('Введите аргументы для расчетов')
    ar = list(input().split())
    print(G(*ar))

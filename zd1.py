#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Написать функцию, вычисляющую среднее
геометрическое своих аргументов
"""


def G(*args):
    if args:
        p = 1
        for i in args:
            p *= i
        p = p ** (1 / len(args))
        return p
    else:
        return None


if __name__ == "__main__":
    ar = list(map(int, input('Введите данные:\n').split()))
    print('Среднее геометрическое', G(*ar))

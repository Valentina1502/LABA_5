#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def G(*args):
    if args:
        # list comprehension (генератр списков)
        values = [int(arg) for arg in args]

        n = len(values)
        i, summ = 0, 0
        for i, value in enumerate(values, 0):
            summ += 1/value
        garm = n/summ
        garm = '{:.4f}'.format(garm)
        return garm
    else:
        return None


if __name__ == "__main__":
    print('Введите через прбел аргументы для расчетов')
    ar = input().split()
    print(G(*ar))

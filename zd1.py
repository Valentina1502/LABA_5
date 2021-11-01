#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def G(*args):
    if args:
        # list comprehension (генератр списков)
        values = [int(arg) for arg in args]

        n = len(values)
        i, p = 1, 1
        for i, value in enumerate(values, 0):
            p *= value
        g = pow(p, (1/(n)))
        g = '{:.4f}'.format(g)
        return g
    else:
        return None


if __name__ == "__main__":
    print('Введите через прбел аргументы для расчетов')
    ar = input().split()
    print(G(*ar))

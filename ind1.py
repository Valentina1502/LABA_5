#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def G(*args):
    if args:

        summ = 0
        for i, value in enumerate(args):
            if int(value) > 0:
                for value2 in args[i + 1:]:
                    summ += int(value2)
                return summ

    else:
        return None


if __name__ == "__main__":
    print('Введите через прбел аргументы для расчетов')
    ar = list(input().split())
    print(G(*ar))

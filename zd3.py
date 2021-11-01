#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def cat(**kwargs):
    sum, sr = 0, 0
    n = len(kwargs)
    max = 0
    for items, value in kwargs.items():
        sum += kwargs[items]
        if kwargs[items] > max:
            max = kwargs[items]
            name = items
    sr = sum / n
    sr = '{:.2f}'.format(sr)

    print(f'Самый толстый кот - {name} - весит {max} кг')
    print(f'В среднем каждый кот весит {sr} кг')


if __name__ == '__main__':
    cat(Афина=7.1, Мафин=12.4, Том=10.8,
        Финик=2.4, Семен=8.9, Персик=3.5, Марго=6.7)

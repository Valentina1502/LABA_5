#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Задан список котов и их вес в килограммах.
Необходимо определить самого крупного
кота и средний вес каждого
"""


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
    return (sr, max, name)

if __name__ == '__main__':
    ca = cat(
        Афина=7.1,
        Мафин=12.4,
        Том=10.8,
        Финик=2.4,
        Семен=8.9,
        Персик=3.5,
        Марго=6.7
    )
    print(f'Самый толстый кот - {ca[2]} - весит {ca[1]} кг')
    print(f'В среднем каждый кот весит {ca[0]} кг')

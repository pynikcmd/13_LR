#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def geometric_mean(*args):
    if args:
        values = [float(arg) for arg in args]
        koren = 1/len(values)
        mul = 1
        for x in values:
            mul *= x
        return mul ** koren
    else:
        return None


if __name__ == '__main__':
    print(geometric_mean())
    print(geometric_mean(2, 1, 2, 3))
    print(geometric_mean(3, 7, 1, 6, 9))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def harmonic_mean(*args):
    if args:
        values = [float(arg) for arg in args]
        n = len(values)
        znam = 0
        for x in values:
            znam += 1/x
        return n/znam
    else:
        return None


if __name__ == '__main__':
    print(harmonic_mean())
    print(harmonic_mean(2, 1, 2, 3))
    print(harmonic_mean(3, 7, 1, 6, 9))

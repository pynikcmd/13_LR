# !/usr/bin/env python3
# -*- coding: utf-8 -*-


def sum_after_max(*args):
    """
    Сумму аргументов, расположенных после максимального аргумента.
    """
    if args:
        values = [float(arg) for arg in args]
        maxi = -1
        maxi_idx = 0
        for i, item in enumerate(values):
            if item > maxi:
                maxi_idx = i
                maxi = item
        return sum(values[maxi_idx+1:])
    else:
        return None


if __name__ == "__main__":
    print("Сумму аргументов, расположенных после максимального аргумента: ",
          sum_after_max(4.23, 52, 2.22, 7.4, 5.2, 2.23))

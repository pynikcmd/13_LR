# !/usr/bin/env python3
# -*- coding: utf-8 -*-


def pet(**kwargs):
    for key, value in kwargs.items():
        if value == 1:
            print("{} завел(-а) {} котика".format(key, value))
        elif value > 20:
            if (value % 10) in [1, 2, 3, 4]:
                print("{} завел(-а) {} котика".format(key, value))
            else:
                print("{} завел(-а) {} котиков".format(key, value))
        else:
            print("{} завел(-а) {} котиков".format(key, value))
    else:
        return None


if __name__ == "__main__":
    pet(
        Маша=220,
        Света=201,
        Вика=122,
        Гамид=103,
        Яна=204,
    )

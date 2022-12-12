#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    dict_1 = {
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight'
    }

    dict_items = dict_1.items()

    dict_2 = {v: k for k, v in dict_items}

    print(dict_2)

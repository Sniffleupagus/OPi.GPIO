# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull
# See LICENSE.md for details.

import functools
from copy import deepcopy
from OPi.constants import BOARD, BCM, SUNXI, CUSTOM


class _sunXi(object):

    def __getitem__(self, value):

        offset = ord(value[1]) - 65
        pin = int(value[2:])

        assert value[0] == "P"
        assert 0 <= offset <= 25
        assert 0 <= pin <= 31

        return (offset * 32) + pin


_pin_map = {
    # Physical pin to actual GPIO pin
    BOARD: {
        3: 264,
        5: 263,
        7: 269,
        8: 224,
        10: 225,
        11: 226,
        12: 257,
        13: 227,
        15: 261,
        16: 270,
        18: 228,
        19: 231,
        21: 232,
        22: 262,
        23: 230,
        24: 229,
        26: 233,
        27: 266,
        28: 265,
        29: 256,
        31: 271,
        32: 267,
        33: 268,
        35: 258,
        36: 76,
        37: 272,
        38: 260,
        39: 259
    },

    # BCM pin to actual GPIO pin
    BCM: {
         0: 266, # _pin_map[BOARD][27],
         1: 265, # _pin_map[BOARD][28],
         2: 264, # _pin_map[BOARD][3],
         3: 263, # _pin_map[BOARD][5],
         4: 269, # _pin_map[BOARD][7],
         5: 256, # _pin_map[BOARD][29],
         6: 271, # _pin_map[BOARD][31],
         7: 269, # _pin_map[BOARD][26],
         8: 229, # _pin_map[BOARD][24],
         9: 232, # _pin_map[BOARD][21],
        10: 231, # _pin_map[BOARD][19],
        11: 230, # _pin_map[BOARD][23],
        12: 267, # _pin_map[BOARD][32],
        13: 268, # _pin_map[BOARD][33],
        14: 224, # _pin_map[BOARD][8],
        15: 225, # _pin_map[BOARD][10],
        16:  76, # _pin_map[BOARD][36],
        17: 226, # _pin_map[BOARD][11],
        18: 257, # _pin_map[BOARD][12],
        19: 258, # _pin_map[BOARD][35],
        20: 260, # _pin_map[BOARD][38],
        21: 259, # _pin_map[BOARD][40],
        22: 261, # _pin_map[BOARD][15],
        23: 270, # _pin_map[BOARD][16],
        24: 228, # _pin_map[BOARD][18],
        25: 262, # _pin_map[BOARD][22],
        26: 272, # _pin_map[BOARD][37],
        27: 227, # _pin_map[BOARD][13]
    },

    SUNXI: _sunXi(),

    # User defined, initialized as empty
    CUSTOM: {}
}


def set_custom_pin_mappings(mappings):
    _pin_map[CUSTOM] = deepcopy(mappings)


def get_gpio_pin(mode, channel):
    assert mode in [BOARD, BCM, SUNXI, CUSTOM]
    return _pin_map[mode][channel]


bcm = functools.partial(get_gpio_pin, BCM)
board = functools.partial(get_gpio_pin, BOARD)
sunxi = functools.partial(get_gpio_pin, SUNXI)
custom = functools.partial(get_gpio_pin, CUSTOM)

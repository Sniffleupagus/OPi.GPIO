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
        3:  192 + 16, # G=192
        5:  192 + 15,
        7:  192 + 19,
        8:  192 + 6,
        10: 192 + 7,
        11: 224 + 2, # H = 224
        12: 192 + 11,
        13: 224 + 3,
        15: 192 + 2,
        16: 192 + 8,
        18: 192 + 9,
        19: 224 + 7,
        21: 224 + 8,
        22: 192 + 1,
        23: 224 + 6,
        24: 224 + 5,
        26: 224 + 9,
        27: 192 + 18,
        28: 192 + 17,
        29: 192 + 3,
        31: 192 + 4,
        32: 192 + 0,
        33: 192 + 5,
        35: 192 + 12,
        36: 224 + 4,
        37: 192 + 10,
        38: 192 + 14,
        40: 192 + 13
    },

    # BCM pin to actual GPIO pin
    BCM: {
         0: 192+18, # _pin_map[BOARD][27],
         1: 192+17, # _pin_map[BOARD][28],
         2: 192+16, # _pin_map[BOARD][3],
         3: 192+15, # _pin_map[BOARD][5],
         4: 192+19, # _pin_map[BOARD][7],
         5: 192+3, # _pin_map[BOARD][29],
         6: 192+4, # _pin_map[BOARD][31],
         7: 224+9, # _pin_map[BOARD][26],
         8: 224+5, # _pin_map[BOARD][24],
         9: 224+8, # _pin_map[BOARD][21],
        10: 224+7, # _pin_map[BOARD][19],
        11: 224+6, # _pin_map[BOARD][23],
        12: 192+0, # _pin_map[BOARD][32],
        13: 192+5, # _pin_map[BOARD][33],
        14: 192+6, # _pin_map[BOARD][8],
        15: 192+7, # _pin_map[BOARD][10],
        16: 224+4, # _pin_map[BOARD][36],
        17: 224+2, # _pin_map[BOARD][11],
        18: 192+11, # _pin_map[BOARD][12],
        19: 192+12, # _pin_map[BOARD][35],
        20: 192+14, # _pin_map[BOARD][38],
        21: 192+13, # _pin_map[BOARD][40],
        22: 192+2, # _pin_map[BOARD][15],
        23: 192+8, # _pin_map[BOARD][16],
        24: 192+9, # _pin_map[BOARD][18],
        25: 192+1, # _pin_map[BOARD][22],
        26: 192+10, # _pin_map[BOARD][37],
        27: 224+3, # _pin_map[BOARD][13]
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
